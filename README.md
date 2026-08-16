# 🏫 School Assistant Telegram Bot

A Telegram bot that helps students and parents quickly find:
- which teachers teach a given subject,
- which classroom (cabinet) each teacher is in.

It also links out to a curated study-materials website. Built to solve a
real, everyday problem at my school — new students and parents often don't
know which teacher to look for or where their classroom is.

## ✨ Features

- 📚 **Subject menu** — pick any of 13 school subjects from an inline keyboard
- 👨‍🏫 **Teacher lookup** — see which teachers teach that subject
- 📍 **Classroom info** — instantly get the teacher's cabinet number
- 🔗 **Study materials** — quick link to a study-resources website
- 🧭 **Simple navigation** — back buttons at every step, no typing required

## 🛠 Tech stack

- Python 3
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (`telebot`)
- `python-dotenv` for safe configuration (no secrets hardcoded in source)

## 📂 Project structure

```
school-assistant-bot/
├── bot.py            # Entry point — starts the bot
├── config.py         # Loads the bot token from environment variables
├── data.py           # Subjects, teachers, and classroom data
├── keyboards.py       # Builds the inline keyboards (menus)
├── handlers.py        # /start, /help, and button-press logic
├── requirements.txt   # Python dependencies
├── .env.example       # Template for your local .env file
└── .gitignore
```

The code is split into small modules on purpose: `data.py` holds the school
data separately from the bot logic, so updating next year's teacher list
doesn't require touching any code that talks to Telegram.

## 🚀 Getting started

### 1. Clone the repository
```bash
git clone https://github.com/mksmedvedmain-boop/School-Assistant-Telegram-Bot.git
cd School-Assistant-Telegram-Bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a bot token
Message [@BotFather](https://t.me/BotFather) on Telegram, run `/newbot`,
and follow the instructions to get a token.

### 4. Set up your environment
```bash
cp .env.example .env
```
Then open `.env` and paste your token:
```
BOT_TOKEN=your_telegram_bot_token_here
```

### 5. Run the bot
```bash
python bot.py
```

## 🔒 Security note

The bot token is loaded from an environment variable, never hardcoded in
the source code, and `.env` is excluded via `.gitignore`. This prevents the
token from ever being exposed in the git history.

## 🗺 Possible future improvements

- Add a database (SQLite) for teacher schedules and homework reminders
- Add a search-by-teacher-name feature
- Deploy the bot on a free host (Railway / Render) so it runs 24/7
- Add unit tests for the handlers

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE).
