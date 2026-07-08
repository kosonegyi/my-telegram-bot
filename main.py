import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Render Environment Variables ထဲတွင် TOKEN ရှိရပါမည်
TOKEN = os.getenv('TOKEN') 
ADMIN_ID = 7303908979
CHANNEL_ID = "-1003669384087" 
MATCHES_FILE = "matches.txt"

def get_matches_text():
    if os.path.exists(MATCHES_FILE):
        with open(MATCHES_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return content if content else "⚽️ လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"
    return "⚽️ လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"

async def update_matches(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("❌ သင်သည် Admin မဟုတ်ပါ။")
        return
    new_text = " ".join(context.args)
    if not new_text:
        await update.message.reply_text("စာသားထည့်ရန်လိုအပ်ပါသည်။ ဥပမာ - /update_matches ⚽️ မန်ယူ vs လီဗာပူး")
        return
    with open(MATCHES_FILE, "w", encoding="utf-8") as f:
        f.write(new_text)
    await update.message.reply_text("✅ ပွဲစဉ်များ အောင်မြင်စွာ ပြင်ဆင်ပြီးပါပြီ။")

def get_main_text():
    return (
        "🔥 <b>ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        "✨ <b>မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ 👇"
    )

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("⚽ ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton("💰 ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton("🎁 Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    await update.message.reply_text(get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

async def broadcast(update, context):
    keyboard = [
        [InlineKeyboardButton("⚽ ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton("💰 ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
        [InlineKeyboardButton("🎁 Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]
    try:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
        await update.message.reply_text("✅ Channel ထဲသို့ အောင်မြင်စွာ ပို့ပြီးပါပြီ။")
    except Exception as e:
        await update.message.reply_text(f"❌ အမှားတစ်ခုဖြစ်နေပါသည်။ Bot ကို Channel Admin ပေးထားပါသလား စစ်ဆေးပါ။\nError: {e}")

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == 'matches':
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 နောက်သို့", callback_data='start')]]))
    elif query.data == 'deposit':
        await query.message.edit_text("💸 <b>ငွေသွင်း/ငွေထုတ်ရန်အတွက်</b> Admin <a href='https://t.me/kothu7877'>@kothu7877</a> ကို ဆက်သွယ်ပေးပါ။", parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 နောက်သို့", callback_data='start')]]))
    elif query.data == 'start':
        keyboard = [
            [InlineKeyboardButton("⚽ ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
            [InlineKeyboardButton("💰 ငွေသွင်း/ငွေထုတ်", callback_data='deposit')],
            [InlineKeyboardButton("🎁 Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
        ]
        await query.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("update_matches", update_matches))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
