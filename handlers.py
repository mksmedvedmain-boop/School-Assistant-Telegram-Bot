"""
Telegram message and callback handlers for the School Assistant Bot.

register_handlers(bot) attaches every handler to the given TeleBot instance.
Keeping registration in a function (instead of using @bot.message_handler at
import time on a global bot object) makes the code easier to test and reuse.
"""

from telebot import types

from data import TEACHERS, CABINETS, CHEAT_SHEETS_URL
from keyboards import subjects_menu, teachers_menu, back_menu, cheats_menu


def register_handlers(bot):

    @bot.message_handler(commands=["start"])
    def start(message: types.Message):
        user_name = message.from_user.first_name
        bot.send_message(
            message.chat.id,
            f"👋 Привет, {user_name}!\n\n"
            "Я помогу найти учителя, его кабинет и учебные материалы.\n"
            "Выбери предмет:",
            reply_markup=subjects_menu(),
        )

    @bot.message_handler(commands=["help"])
    def help_command(message: types.Message):
        bot.send_message(
            message.chat.id,
            "ℹ️ Как пользоваться ботом:\n"
            "1. Нажми /start\n"
            "2. Выбери предмет из списка\n"
            "3. Выбери преподавателя — бот покажет номер кабинета\n"
            "4. Кнопка «📚 Шпаргалки» откроет учебные материалы",
        )

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call: types.CallbackQuery):
        data = call.data

        if data == "cheats":
            bot.edit_message_text(
                f"📚 Шпаргалки и учебные материалы:\n\n{CHEAT_SHEETS_URL}",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=cheats_menu(),
            )

        elif data in TEACHERS:
            bot.edit_message_text(
                f"📘 {data}\nВыберите преподавателя:",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=teachers_menu(data),
            )

        elif data in CABINETS:
            bot.edit_message_text(
                f"👨‍🏫 {data}\n📍 {CABINETS[data]}",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=back_menu(),
            )

        elif data == "back":
            bot.edit_message_text(
                "Выбери предмет:",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=subjects_menu(),
            )

        else:
            bot.answer_callback_query(call.id, "Ошибка выбора")
