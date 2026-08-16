"""
School Assistant Telegram Bot — entry point.

Run this file to start the bot:
    python bot.py

Make sure you've created a .env file with your BOT_TOKEN first
(see .env.example and README.md).
"""

import telebot

from config import BOT_TOKEN
from handlers import register_handlers


def main():
    bot = telebot.TeleBot(BOT_TOKEN)
    register_handlers(bot)

    print("Bot is running... Press Ctrl+C to stop.")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
