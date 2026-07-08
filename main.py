import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Token ကို Render ၏ Environment Variables တွင် ထည့်ရပါမည်
TOKEN = os.environ.get('import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Token ကို Render ၏ Environment Variables တွင် ထည့်ရပါမည်
TOKEN = os.environ.get('8897020821:AAFYPCopRI84EzIK5GstAM99Edo5Pz0Sq18')
CHANNEL_ID = '-1003669384087'

def get_main_text():
    return (
        "<b> ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        "<b> မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ "
    )

def get_matches_text():
    return (
        "<b> ဒီနေ့ပွဲစဉ်များ</b>\n"
        "--------------------------\n"
        " <b>..........</b> vs <b>..............</b>\n"
        "<i> .............</i>\n\n"
        " <b>..............</b> vs <b>............</b>\n"
        "<i> ................</i>\n"
        "--------------------------"
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
    await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" နောက်သို့", callback_data='start')]]))
    elif query.data == 'deposit':
        await query.message.edit_text(" <b>ငွေသွင်း/ငွေထုတ်ရန်အတွက်</b> Admin <a href='https://t.me/kothu7877'>@kothu7877</a> ကို ဆက်သွယ်ပေးပါ။", parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" နောက်သို့", callback_data='start')]]))
    elif query.data == 'start':
        await query.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')], [InlineKeyboardButton(" ငွေသွင်း/ငွေထုတ်", callback_data='deposit')], [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]]))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()')
CHANNEL_ID = '-1003669384087'

def get_main_text():
    return (
        "<b> ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        "<b> မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ "
    )

def get_matches_text():
    return (
        "<b> ဒီနေ့ပွဲစဉ်များ</b>\n"
        "--------------------------\n"
        " <b>..........</b> vs <b>..............</b>\n"
        "<i> .............</i>\n\n"
        " <b>..............</b> vs <b>............</b>\n"
        "<i> ................</i>\n"
        "--------------------------"
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
    await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" နောက်သို့", callback_data='start')]]))
    elif query.data == 'deposit':
        await query.message.edit_text(" <b>ငွေသွင်း/ငွေထုတ်ရန်အတွက်</b> Admin <a href='https://t.me/kothu7877'>@kothu7877</a> ကို ဆက်သွယ်ပေးပါ။", parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" နောက်သို့", callback_data='start')]]))
    elif query.data == 'start':
        await query.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')], [InlineKeyboardButton(" ငွေသွင်း/ငွေထုတ်", callback_data='deposit')], [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]]))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
