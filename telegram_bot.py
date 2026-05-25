import telebot
import os

from dotenv import load_dotenv

from memory_service import process_memory

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def save_from_telegram(message):

    content = message.text

    result = process_memory(content)

    if not result:

        bot.reply_to(
            message,
            "⚠️ Mensaje vacío."
        )

        return

    bot.reply_to(
        message,
        f"""
🧠 Memoria guardada

📌 {content}

🔥 Prioridad: {result["priority"]}

🗂 Tipo: {result["type"]}

📅 Fecha: {result["detected_date"]}
"""
    )


print("🤖 HELIOS Telegram Bot iniciado...")

bot.infinity_polling()