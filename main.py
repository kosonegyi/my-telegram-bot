import os
import asyncio
from threading import Thread
from flask import Flask
import logging
import re
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

app = Flask('')

@app.route('/')
def home():
    return "Bot is running successfully!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

ADMIN_ID = 7303908979
TOKEN = "8823110888:AAHDx1xixNUwVKBjme0-90iok0YfRPNH03k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💎 Diamond ဝယ်မည်", callback_data="buy_diamond")],
        [InlineKeyboardButton("📖 ဈေးဝယ်နည်းလမ်း", callback_data="guide")],
        [InlineKeyboardButton("📞 ဆက်သွယ်ရန်", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"မင်္ဂလာပါ {user.first_name} ✨\n\n"
        "မြန်မာနိုင်ငံအတွက် Mobile Legends Diamond များကို စိတ်ချယုံကြည်စွာ ဝယ်ယူနိုင်သော စတိုးဆိုင်မှ ကြိုဆိုပါတယ်။"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "buy_diamond":
        await query.message.reply_text("ကျေးဇူးပြု၍ ဝယ်ယူလိုသော Game ID နှင့် Zone ID ကို ပေးပို့ပါ။")
    elif query.data == "guide":
        await query.message.reply_text("ဈေးဝယ်ယူရန် ငွေပေးချေမှုပုံစံများကို ဆက်လက်လုပ်ဆောင်ပါ။")
    elif query.data == "contact":
        await query.message.reply_text("အရေးပေါ်ဆက်သွယ်ရန် Admin: @kosonegyi သို့ ဆက်သွယ်နိုင်ပါသည်။")

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    keep_alive()
    application.run_polling()

if __name__ == '__main__':
    main()
