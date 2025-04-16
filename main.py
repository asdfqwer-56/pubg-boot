import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("تحميل ملف سكن ببجي", url="https://example.com/pubg-skin.zip")]
    ]
    await update.message.reply_text("أهلاً بك في بوت تحميل سكنات ببجي!", reply_markup=InlineKeyboardMarkup(buttons))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
