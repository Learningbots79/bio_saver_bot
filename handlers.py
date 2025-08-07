from telegram import Update
from telegram.ext import (
    ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler
)
from database import load_bios, save_bios, delete_bios, get_bios, set_bios

SET_BIO = 1

# == start command ==
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hey you are in Bio Saver Bot\n\n"
        "/setbio - Save your bio\n"
        "/view - View your bio\n"
        "/delete - Delete your bio\n"
        "/cancel - Cancel during bio setting"
    )

# == start saving bio ==
async def set_bio_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your bio message to save 📜")
    return SET_BIO

# == saving bio part ==
async def set_bio_save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bio_text = update.message.text
    user_id = update.effective_user.id
    set_bios(user_id, bio_text)
    await update.message.reply_text("Your bio saved")
    return ConversationHandler.END

# == cancel command if want to stop during saving message ==
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bio saving cancelled:")
    return ConversationHandler.END

# == view bio ==
async def view_bio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    data = get_bios(user_id)
    if data:
        await update.message.reply_text(f"📜 Your bio : {data}")
    else:
        await update.message.reply_text("You haven't save any bio ❌")

# == delete bio ==
async def delete_bio_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if delete_bios(user_id):
        await update.message.reply_text("Your bio deleted 🗑️")
    else:
        await update.message.reply_text("You didn't have bio to delete ⚠️")

# == command handler ==
def cmd_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("view", view_bio),
        CommandHandler("delete", delete_bio_cmd),
        ConversationHandler(
            entry_points=[CommandHandler("setbio", set_bio_start)],
            states={SET_BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_bio_save)]},
            fallbacks=[CommandHandler("cancel", cancel)]
        )
    ]
