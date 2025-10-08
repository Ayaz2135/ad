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

    app = Application.builder().token(AD_BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))

    logger.info("✅ Bot is starting...")
    await app.run_polling()  # This internally handles init/start/shutdown safely


# --- Safe Runner for Render or Local ---
def safe_async_run(coro):
    """Run async code safely in Render or any already-running loop."""
    try:
        asyncio.run(coro)
    except RuntimeError as e:
        if "already running" in str(e):
            # Use nest_asyncio to reuse existing loop
            import nest_asyncio
            nest_asyncio.apply()
            loop = asyncio.get_event_loop()
            loop.create_task(coro)
            loop.run_forever()
        else:
            raise


if __name__ == "__main__":
    safe_async_run(main())
