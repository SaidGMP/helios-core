import telebot
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TOKEN)


def send_telegram_message(message):

    try:

        bot.send_message(
            CHAT_ID,
            message
        )

    except Exception as e:

        print(
            f"Telegram error: {e}"
        )