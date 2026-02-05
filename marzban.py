import requests
from datetime import datetime, timedelta
from config import MARZBAN_URL, MARZBAN_API_TOKEN

HEADERS = {
    "Authorization": f"Bearer {MARZBAN_API_TOKEN}",
    "Content-Type": "application/json"
}


def create_user(username: str, days: int):
    expire = datetime.utcnow() + timedelta(days=days)

    payload = {
        "username": username,
        "expire": int(expire.timestamp()),
        "data_limit": 0,
        "proxies": {
            "vless": {}
        }
    }

    r = requests.post(
        f"{MARZBAN_URL}/api/user",
        headers=HEADERS,
        json=payload,
        timeout=10
    )
    r.raise_for_status()
    return expire


def extend_user(username: str, current_expire: str, days: int):
    base = datetime.fromisoformat(current_expire)
    new_expire = base + timedelta(days=days)

    payload = {
        "expire": int(new_expire.timestamp())
    }

    r = requests.put(
        f"{MARZBAN_URL}/api/user/{username}",
        headers=HEADERS,
        json=payload,
        timeout=10
    )
    r.raise_for_status()
    return new_expire


def get_subscription_link(username: str):
    return f"{MARZBAN_URL}/sub/{username}"
