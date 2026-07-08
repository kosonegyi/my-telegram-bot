import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Logging ထည့်သွင်းခြင်း (Error များကို သိရှိနိုင်ရန်)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start command ပို့လိုက်လျှင် Menu ခလုတ်များ ပေါ်လာစေရန်
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton("ငွေသွင်း/ငွေထုတ်", callback_data='money')],
        [InlineKeyboardButton("Admin ထံမှ Bonus ရယူရန်", url='https://t.me/your_admin_username')] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('မင်္ဂလာပါ! Area 69 မှ ကြိုဆိုပါတယ်။ အောက်ပါတို့ကို ရွေးချယ်နိုင်ပါသည်။', reply_markup=reply_markup)

# ခလုတ်များကို နှိပ်လိုက်သောအခါ ဖြစ်ပေါ်မည့် အလုပ်များ
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'matches':
        await query.edit_message_text(text="ဒီနေ့ပွဲစဉ်များမှာ - [ဤနေရာတွင် ပွဲစဉ်များ ထည့်ပါ]")
    elif query.data == 'money':
        await query.edit_message_text(text="ငွေသွင်း/ငွေထုတ်ရန် Admin ကို တိုက်ရိုက်ဆက်သွယ်ပါ။")

if __name__ == '__main__':
    # Render ရှိ Environment Variables မှ TOKEN ကို ခေါ်ယူခြင်း
    TOKEN = os.getenv("TOKEN")
    
    if not TOKEN:
        print("Error: TOKEN မတွေ့ရှိပါ။ Environment Variable တွင် သေချာထည့်ပေးပါ။")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        # Handler များ ထည့်သွင်းခြင်း (အရေးကြီးဆုံးအပိုင်း)
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_click)) # ခလုတ်နှိပ်လျှင် အလုပ်လုပ်စေရန်
        
        print("Bot စတင်နေပါပြီ...")
        app.run_polling()
