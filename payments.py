import uuid

def create_invoice(amount: int):
    invoice_id = str(uuid.uuid4())
    pay_url = f"https://PAYMENT_GATEWAY/pay/{invoice_id}"
    return invoice_id, pay_url
