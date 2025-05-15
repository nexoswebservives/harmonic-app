
import os
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "SEU_TOKEN_AQUI")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "SEU_CHAT_ID_AQUI")

def enviar_mensagem_telegram(mensagem: str):
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=mensagem)
    except Exception as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")
