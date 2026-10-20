import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

# .env ဖိုင်ထဲက လျှို့ဝှက်ချက်များကို စတင်ဖတ်ရန်
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot အလုပ်လုပ်နေပါပြီ!')

if __name__ == '__main__':
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN ကို .env (သို့မဟုတ်) Environment Variables ထဲတွင် ထည့်သွင်းပေးပါ။")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()
