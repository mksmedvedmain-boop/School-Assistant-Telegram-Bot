"""
Configuration for the School Assistant Telegram Bot.

The bot token is NEVER hardcoded here. It is loaded from an environment
variable (BOT_TOKEN), which you set in a local .env file (see .env.example)
or in your hosting provider's "environment variables" / "secrets" settings.

This is a security best practice: hardcoded tokens end up in git history
and can be stolen by anyone who sees the repository.
"""

import os
from dotenv import load_dotenv

# Loads variables from a local .env file, if one exists.
# On a server (Railway, Render, etc.) you'd set BOT_TOKEN in the
# platform's dashboard instead, and this line simply does nothing.
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN is not set.\n"
        "1. Copy .env.example to .env\n"
        "2. Paste your Telegram bot token into .env\n"
        "3. Run the bot again"
    )
