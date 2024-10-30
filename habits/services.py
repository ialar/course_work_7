import requests

from config import settings


def send_tg_message(chat_id, message):
    """Отправляет сообщение в телеграм."""
    params = {"text": message, "chat_id": chat_id}
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )
