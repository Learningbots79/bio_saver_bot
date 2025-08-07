from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers import cmd_handlers

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    for handler in cmd_handlers():
        app.add_handler(handler)

    print("🤖 Bot started.....")
    app.run_polling()

if __name__ == "__main__":
    main()
