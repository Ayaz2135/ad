# main.py
import logging
from telegram.ext import Application, CommandHandler
from config import AD_BOT_TOKEN
from database import init_db
from handlers.user import start
from handlers.admin import broadcast

# Initialize database
init_db()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def main():
    app = Application.builder().token(AD_BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))

    print("✅ Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
