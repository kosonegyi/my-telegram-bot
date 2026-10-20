import os
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Flask app for Keep Alive (Render)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running successfully!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Telegram Bot Token and Admin ID
TOKEN = "8823110888:AAE0kS0q5FlCNcc8_favoo5VRDW5uW7Dl9s"
ADMIN_ID = "7303908979"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    # အောက်ခြေခလုတ်များ (ReplyKeyboardMarkup)
    keyboard = [
        ["💎 Diamond ဝယ်မည်"],
        ["📖 ဈေးဝယ်နည်းလမ်း"],
        ["📞 ဆက်သွယ်ရန်"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    welcome_text = (
        f"မင်္ဂလာပါ {user.first_name} ✨\n\n"
        "မြန်မာနိုင်ငံအတွက် Mobile Legends Diamondများကို စိတ်ချယုံကြည်စွာ ဝယ်ယူနိုင်ပါပြီ။\n"
        "အောက်ပါခလုတ်များမှ လိုအပ်သည်များကို ရွေးချယ်ပါ။"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

def main():
    keep_alive()
    
    # Run bot using application builder
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
