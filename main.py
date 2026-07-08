import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Render Environment Variables ထဲတွင် TOKEN ရှိရပါမည်
TOKEN = os.getenv('TOKEN') 
ADMIN_ID = 7303908979
CHANNEL_ID = "-1003669384087" 
MATCHES_FILE = "matches.txt"

# ဖုန်းထဲတွင် Copy ကူးပါက စတစ်ကာများ ပျောက်ပျက်မသွားစေရန် နံပါတ်ကုတ်ဖြင့် ပြောင်းလဲသတ်မှတ်ခြင်း
E_FIRE = chr(128293)       # 
E_SPARKLE = chr(10024)     # 
E_DOWN = chr(128071)       # 
E_BALL = chr(9917)         # 
E_MONEY = chr(128176)      # 
E_GIFT = chr(127873)       # 
E_BACK = chr(128281)       # 
E_CHAT = chr(128172)       # 
E_FLY_MONEY = chr(128184)  # 

def get_matches_text():
    if os.path.exists(MATCHES_FILE):
        with open(MATCHES_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return content if content else f"{E_BALL} လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"
    return f"{E_BALL} လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"

def get_main_text():
    return (
        f"{E_FIRE} <b>ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        f"{E_SPARKLE} <b>မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        f"အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ {E_DOWN}"
    )

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton(f"{E_BALL} ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton(f"{E_MONEY} ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton(f"{E_GIFT} Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    await update.message.reply_text(get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

async def broadcast(update, context):
    keyboard = [
        [InlineKeyboardButton(f"{E_BALL} ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton(f"{E_MONEY} ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton(f"{E_GIFT} Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    try:
        # Channel ထဲသို့ စတစ်ကာများနှင့်တကွ စနစ်တကျ ပို့ပေးမည်ဖြစ်သည်
        await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
        await update.message.reply_text(" Channel ထဲသို့ အောင်မြင်စွာ ပို့ပြီးပါပြီ။")
    except Exception as e:
        await update.message.reply_text(f" အမှားဖြစ်နေပါသည်: {e}")

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        keyboard = [[InlineKeyboardButton(f"{E_BACK} နောက်သို့", callback_data='start')]]
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'deposit':
        keyboard = [[InlineKeyboardButton(f"{E_CHAT} Admin ထံ စာပို့ရန်", url='https://t.me/kothu7877')],
                    [InlineKeyboardButton(f"{E_BACK} နောက်သို့", callback_data='start')]]
        await query.message.edit_text(f"{E_FLY_MONEY} <b>ငွေသွင်း/ငွေထုတ်ရန်အတွက်</b> အောက်ပါခလုတ်ကို နှိပ်ပြီး Admin ထံ ဆက်သွယ်ပါ။", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'start':
        keyboard = [
            [InlineKeyboardButton(f"{E_BALL} ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
            [InlineKeyboardButton(f"{E_MONEY} ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
            [InlineKeyboardButton(f"{E_GIFT} Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
        ]
        await update.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
