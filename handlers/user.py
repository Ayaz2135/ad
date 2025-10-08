# handlers/user.py
from telegram import Update
from telegram.ext import ContextTypes
from database import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username, user.first_name)
    await update.message.reply_text(f"👋 Hello {user.first_name}! Welcome to the Ad Bot.")
