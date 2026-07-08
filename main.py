import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# TOKEN ကို Render ၏ Environment Variables ထဲမှာပဲ ထည့်ထားပါ
TOKEN = os.environ.get('TOKEN')
CHANNEL_ID = '-1003669384087'

def get_main_text():
    return (
        "<b> ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        "<b> မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ "
    )

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton(" ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    await update.message.reply_text(get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
