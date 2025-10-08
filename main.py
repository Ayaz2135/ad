import logging
import asyncio
from telegram.ext import Application, CommandHandler
from config import AD_BOT_TOKEN
from database import init_db
from handlers.user import start
from handlers.admin import broadcast

# --- Initialize Database ---
init_db()

# --- Enable Logging ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main():
    """Start the Telegram bot."""
    logger.info("Initializing bot...")

    # Build the application
    app = Application.builder().token(AD_BOT_TOKEN).build()

    # --- Register command handlers ---
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))

    logger.info("✅ Bot is starting...")

    # Start polling
    await app.initialize()
    await app.start()
    logger.info("🚀 Bot is now running and polling for updates...")

    await app.run_polling(stop_signals=None)  # Prevents double stop on Render

    # Clean shutdown (important for Render)
    await app.stop()
    await app.shutdown()
    logger.info("🛑 Bot stopped cleanly.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("🛑 Bot stopped manually.")
