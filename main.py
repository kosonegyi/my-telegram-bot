import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

TOKEN = os.getenv('TOKEN') 
ADMIN_ID = 7303908979
CHANNEL_ID = "-1003669384087" 
MATCHES_FILE = "matches.txt"

def get_matches_text():
    if os.path.exists(MATCHES_FILE):
        with open(MATCHES_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return content if content else " လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"
    return " လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"

def get_main_text():
    return (
        " <b>ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        " <b>မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ "
    )

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton(" ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    await update.message.reply_text(get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

async def broadcast(update, context):
    keyboard = [
        [InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton(" ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    try:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
        await update.message.reply_text(" Channel ထဲသို့ အောင်မြင်စွာ ပို့ပြီးပါပြီ။")
    except Exception as e:
        await update.message.reply_text(f" အမှားဖြစ်နေပါသည်။ Bot ကို Channel Admin ပေးထားပါသလား စစ်ဆေးပါ။\nError: {e}")

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        keyboard = [[InlineKeyboardButton(" နောက်သို့", callback_data='start')]]
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'deposit':
        keyboard = [[InlineKeyboardButton(" Admin ထံ စာပို့ရန်", url='https://t.me/kothu7877')],
                    [InlineKeyboardButton(" နောက်သို့", callback_data='start')]]
        await query.message.edit_text(" <b>ငွေသွင်း/ငွေထုတ်ရန်အတွက်</b> အောက်ပါခလုတ်ကို နှိပ်ပြီး Admin ထံ ဆက်သွယ်ပါ။", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'start':
        keyboard = [
            [InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
            [InlineKeyboardButton(" ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
            [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
        ]
        await query.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast)) # ဒီလိုင်းကို ပြန်ထည့်ထားပါတယ်
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
