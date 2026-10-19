import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# .env ဖိုင်ထဲက လျှို့ဝှက်ချက်များကို စတင်ဖတ်ရန်
load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# လျှို့ဝှက်ချက်များကို .env ထဲမှ လုံခြုံစွာလှမ်းယူခြင်း
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot အလုပ်လုပ်နေပါပြီ!')

if __name__ == '__main__':
    # ကုဒ်ထဲမှာ Token ကို တိုက်ရိုက်မရေးတော့ဘဲ Variable အဖြစ် ပြောင်းလဲထားပါတယ်
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()
