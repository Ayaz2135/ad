# handlers/admin.py
from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID
from database import get_all_users

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to use this command.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /broadcast <message>")
        return

    msg = " ".join(context.args)
    users = get_all_users()
    success = 0
    fail = 0

    await update.message.reply_text(f"📢 Sending broadcast to {len(users)} users...")

    for uid in users:
        try:
            await context.bot.send_message(chat_id=uid, text=msg)
            success += 1
        except:
            fail += 1

    await update.message.reply_text(f"✅ Done! Sent: {success}, Failed: {fail}")
