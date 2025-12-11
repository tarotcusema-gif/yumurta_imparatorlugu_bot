import logging
import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update, context):
    await update.message.reply_text("Bot çalışıyor! 🥚")

async def help_cmd(update, context):
    await update.message.reply_text("Bu bir test yardım komutudur.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    app.run_polling()

if __name__ == "__main__":
    main()
