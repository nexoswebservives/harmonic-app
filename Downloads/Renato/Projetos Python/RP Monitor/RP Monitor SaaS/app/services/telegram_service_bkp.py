import os
from dotenv import load_dotenv
from telegram import Bot

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o token do bot a partir da variável de ambiente
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Instancia o bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

def enviar_mensagem_telegram(mensagem: str, chat_id: str):
    try:
        bot.send_message(chat_id=chat_id, text=mensagem)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
