# main.py
import logging
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

def main():
    """Start the Telegram bot."""
    logger.info("Initializing bot...")

    app = Application.builder().token(AD_BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))

    logger.info("✅ Bot is starting...")
    
    # Use run_polling() directly, it handles asyncio internally
    app.run_polling(stop_signals=None)  # stop_signals=None prevents double stop on Render

if __name__ == "__main__":
    main()
