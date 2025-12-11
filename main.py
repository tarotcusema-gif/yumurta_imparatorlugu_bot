import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "BURAYA_BOT_TOKENİNİ_YAZ"  # BotFather’dan aldığın token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    await update.message.reply_text("🍳 Yumurta İmparatorluğu Botu Aktif!")

async def help_cmd(update, context):
    await update.message.reply_text("Komutlar:\n/start - Botu başlat")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    app.run_polling()

if __name__ == '__main__':
    main()
