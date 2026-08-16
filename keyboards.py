"""
Inline keyboard builders for the School Assistant Bot.

Splitting keyboard-building into its own file keeps handlers.py focused on
"what happens when a button is pressed" rather than "how the buttons look".
"""

from telebot import types
from data import SUBJECTS, TEACHERS, CHEAT_SHEETS_URL


def subjects_menu() -> types.InlineKeyboardMarkup:
    """Main menu: one button per subject, laid out two-per-row, plus cheat sheets."""
    markup = types.InlineKeyboardMarkup()

    # Group subjects two-by-two so the menu doesn't get too tall.
    for i in range(0, len(SUBJECTS) - 1, 2):
        markup.row(
            types.InlineKeyboardButton(SUBJECTS[i], callback_data=SUBJECTS[i]),
            types.InlineKeyboardButton(SUBJECTS[i + 1], callback_data=SUBJECTS[i + 1]),
        )

    # If there's an odd subject left over, add it on its own row.
    if len(SUBJECTS) % 2 == 1:
        markup.row(types.InlineKeyboardButton(SUBJECTS[-1], callback_data=SUBJECTS[-1]))

    markup.row(types.InlineKeyboardButton("📚 Шпаргалки", callback_data="cheats"))
    return markup


def teachers_menu(subject: str) -> types.InlineKeyboardMarkup:
    """List of teachers for a given subject, with a back button."""
    markup = types.InlineKeyboardMarkup()
    for teacher in TEACHERS[subject]:
        markup.row(types.InlineKeyboardButton(f"👨‍🏫 {teacher}", callback_data=teacher))
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    return markup


def back_menu() -> types.InlineKeyboardMarkup:
    """Just a back button, used on the cabinet-info and cheat-sheets screens."""
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    return markup


def cheats_menu() -> types.InlineKeyboardMarkup:
    """Cheat sheets screen: open the resource site, plus a back button."""
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🌐 Открыть сайт", url=CHEAT_SHEETS_URL))
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    return markup
