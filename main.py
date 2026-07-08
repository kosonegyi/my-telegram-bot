import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Render Environment Variables ထဲတွင် TOKEN ရှိရပါမည်
TOKEN = os.getenv('TOKEN') 

# သင့် ID နှင့် Channel ID 
ADMIN_ID = 7303908979
CHANNEL_ID = "-1003669384087"
MATCHES_FILE = "matches.txt"

# ပွဲစဉ်စာသားကို ဖိုင်ထဲကနေ ဖတ်ခြင်း
def get_matches_text():
    if os.path.exists(MATCHES_FILE):
        with open(MATCHES_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return content if content else "⚽️ လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"
    return "⚽️ လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"

# Admin က ပွဲစဉ်ပြင်ခြင်း
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

# မူလ Function များ
def get_main_text():
    return (
        "🔥 <b>ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        "✨ <b>မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ 👇"
    )

def get_keyboard():
    return [
        [InlineKeyboardButton("⚽ ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton("💰 ငွေသွင်း/ငွေထုတ်", url='https://t.me/kothu7877')],
        [InlineKeyboardButton("🎁 Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me/kothu7877')]
    ]

async def start(update, context):
    await update.message.reply_text(get_main_text(), reply_markup=InlineKeyboardMarkup(get_keyboard()), parse_mode='HTML')

# Channel သို့ စာသားလှမ်းပို့ပေးမည့် Broadcast စနစ်
async def broadcast(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("❌ သင်သည် Admin မဟုတ်ပါ။")
        return
        
    try:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(get_keyboard()), parse_mode='HTML')
        await update.message.reply_text("✅ Channel သို့ စာသားကို အောင်မြင်စွာ Broadcast လုပ်ပြီးပါပြီ။")
    except Exception as e:
        await update.message.reply_text(f"❌ အမှားအယွင်းရှိနေပါသည်။ Bot ကို Channel ထဲတွင် Admin ခန့်ထားရန် လိုအပ်သည်။ Error: {e}")

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 နောက်သို့", callback_data='start')]]))
    elif query.data == 'start':
        await query.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(get_keyboard()))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("update_matches", update_matches))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
