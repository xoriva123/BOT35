
import hmac
import hashlib
from fastapi import FastAPI, Request
from aiogram import Bot
from config import PAYMENT_SECRET, TARIFFS
from database import get_payment, mark_payment_paid, get_user, save_user
from marzban import create_user, extend_user, get_subscription_link
from bot import bot, dp
import uvicorn
import asyncio

app = FastAPI()


@app.post("/payment/webhook")
async def payment_webhook(request: Request):
    data = await request.json()

    invoice_id = data["invoice_id"]
    status = data["status"]
    signature = data["signature"]

    raw = f"{invoice_id}{status}".encode()
    check = hmac.new(PAYMENT_SECRET.encode(), raw, hashlib.sha256).hexdigest()

    if check != signature:
        return {"error": "invalid signature"}

    payment = get_payment(invoice_id)
    if not payment or payment[3] == "paid":
        return {"ok": True}

    _, telegram_id, tariff, _ = payment
    days = TARIFFS[tariff]["days"]

    user = get_user(telegram_id)

    if not user:
        username = f"tg_{telegram_id}"
        expire = create_user(username, days)
    else:
        username = user[1]
        expire = extend_user(username, user[2], days)

    save_user(telegram_id, username, expire.isoformat())
    mark_payment_paid(invoice_id)

    link = get_subscription_link(username)
    await bot.send_message(
        telegram_id,
        f"✅ Оплата получена!\n\n"
        f"🔗 Ваша ссылка подписки:\n{link}\n\n"
        f"⏳ Действует до: {expire.date()}"
    )

    return {"ok": True}


async def start():
    await dp.start_polling(bot)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    uvicorn.run(app, host="0.0.0.0", port=8001)
