import os
import asyncio
from threading import Thread
from flask import Flask
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Flask app တည်ဆောက်ခြင်း (Render အတွက် port 8080 ဖွင့်ရန်)
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

# သင့်ရဲ့ Personal Chat ID
ADMIN_ID = "7303908979" 

# /start command ပို့တဲ့အခါ အောက်ခြေခလုတ်များ တိုက်ရိုက်ပြသခြင်း
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛍️ ဝယ်ယူမည် (Products)"],
        ["💎 Dia စျေးနှုန်းများကြည့်ရန်"],
        ["👨‍💻 Admin တိုက်ရိုက်ဆက်သွယ်ရန်"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    welcome_text = (
        "👋 မင်္ဂလာပါ V VV 🙏\n\n"
        "💳 သင့်အတွက် အကောင်းဆုံးနှင့် အမြန်ဆန်ဆုံး ဝန်ဆောင်မှုများ ပေးရန် အသင့်ရှိနေပါသည်။\n\n"
        "👇 အောက်ပါ ခလုတ်များကို နှိပ်၍ ဝန်ဆောင်မှုများကို ကြည့်ရှုနိုင်ပါသည်။"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# ခလုတ်စာသားများနှင့် ဝယ်သူပို့သမျှစာအားလုံးကို ၁၀၀% ကိုင်တွယ်မည့်စနစ်
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_text = update.message.text
    username_display = f"@{user.username}" if user.username else "@None"

    # (၁) Dia စျေးနှုန်းများကြည့်ရန် ခလုတ်နှိပ်လျှင်
    if user_text == "💎 Dia စျေးနှုန်းများကြည့်ရန်":
        price_text = (
            "🔮 Weekly Pass - 7,100 ks\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 Dia 86    -  6,000ks\n"
            "💎 Dia 172   -  12,000ks\n"
            "💎 Dia 257   -  18,000ks\n"
            "💎 Dia 344   -  24,000ks\n"
            "💎 Dia 516   -  36,000ks\n"
            "💎 Dia 706   -  48,000ks\n"
            "💎 Dia 1346  -  90,000ks\n"
            "💎 Dia 1825  -  120,000ks\n"
            "💎 Dia 2195  -  144,000ks\n"
            "💎 Dia 3688  -  240,000ks\n"
            "💎 Dia 5532  -  360,000ks\n"
            "💎 Dia 9288  -  590,000ks\n\n"
            "🔥 Double Diamond Price 💎\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 50 + 50    =  5,000ks\n"
            "💎 150 + 150  =  13,000ks\n"
            "💎 250 + 250  =  19,500ks\n"
            "💎 500 + 500  =  39,500ks\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Payment: KBZ Pay / Wave Pay\n"
            "📞 09967120289 Pyae Sone\n\n"
            "📸 _ငွေလွှဲပြီးပါက ပြေစာ Screenshot ပုံကို ဤ Bot ထဲသို့ တိုက်ရိုက် ပုံရိုက်ပို့ပေးနိုင်ပါသည်_"
        )
        
        buy_keyboard = [["🛍️ ဝယ်ယူမည့် ပမာဏ ရွေးချယ်ရန်"], ["⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်"]]
        reply_markup = ReplyKeyboardMarkup(buy_keyboard, resize_keyboard=True)
        await update.message.reply_text(price_text, reply_markup=reply_markup)
        
        try:
            await context.bot.send_message(chat_id=ADMIN_ID, text=f"💎 Dia စျေးနှုန်းများကြည့်သူ: {user.full_name} ({username_display})")
        except: pass

    # (၂) ဝယ်ယူမည် (Products) ခလုတ်နှိပ်လျှင်
    elif user_text == "🛍️ ဝယ်ယူမည် (Products)" or user_text == "🛍️ ဝယ်ယူမည့် ပမာဏ ရွေးချယ်ရန်":
        choice_text = "👇 **လူကြီးမင်း ဝယ်ယူလိုသော Dia ပမာဏကို ရွေးချယ်ပေးပါရှင် -**"
        
        buy_keyboard = [
            ["🔮 Weekly Pass (7,100 ks)"],
            ["💎 86 Dia (6,197 ks)", "💎 172 Dia (12,476 ks)"],
            ["💎 257 Dia (18,000 ks)", "💎 344 Dia (24,000 ks)"],
            ["💎 516 Dia (36,000 ks)", "💎 706 Dia (48,000 ks)"],
            ["💎 1346 Dia (90,000 ks)", "💎 1825 Dia (120,000 ks)"],
            ["💎 2195 Dia (144,000 ks)", "💎 3688 Dia (240,000 ks)"],
            ["💎 5532 Dia (36,000 ks)", "💎 9288 Dia (590,000 ks)"],
            ["🔥 Double 50+50 (5,000 ks)", "🔥 Double 150+150 (13,000 ks)"],
            ["🔥 Double 250+250 (19,500 ks)", "🔥 Double 500+500 (39,500 ks)"],
            ["⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်"]
        ]
        reply_markup = ReplyKeyboardMarkup(buy_keyboard, resize_keyboard=True)
        await update.message.reply_text(text=choice_text, reply_markup=reply_markup, parse_mode="Markdown")

    # (၃) ဝယ်သူမှ Dia ပမာဏ တစ်ခုခုကို နှိပ်လိုက်လျှင်
    elif "ks)" in user_text:
        invoice_text = (
            f"🛒 **လူကြီးမင်း ရွေးချယ်ထားသော ပမာဏ:**\n"
            f"➔ ✨ **{user_text}**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 **Payment ဆောင်ရွက်ရန် အချက်အလက်:**\n"
            "• KBZ Pay သို့မဟုတ် Wave Pay\n"
            "• 09967120289 (Pyae Sone)\n\n"
            "📸 **ငွေလွှဲပြီးပါက ပြေစာ Screenshot ပုံကို ဤ Bot ထဲသို့ တိုက်ရိုက် ပုံရိုက်ပို့ပေးပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။**"
        )
        await update.message.reply_text(text=invoice_text, parse_mode="Markdown")

        try:
            alert_selection = f"🛒 **ဝယ်ယူရန် ပမာဏရွေးချယ်မှု အသစ်**\n━━━━━━━━━━━━━━━━━━━━\n👤 ဝယ်သူ: {user.full_name} ({username_display})\n💎 ရွေးချယ်သွားသည်: {user_text}"
            await context.bot.send_message(chat_id=ADMIN_ID, text=alert_selection)
        except: pass

    # (၄) ပင်မစာမျက်နှာသို့ ပြန်ရန် နှိပ်လျှင်
    elif user_text == "⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်":
        keyboard = [
            ["🛍️ ဝယ်ယူမည် (Products)"],
            ["💎 Dia စျေးနှုန်းများကြည့်ရန်"],
            ["👨‍💻 Admin တိုက်ရိုက်ဆက်သွယ်ရန်"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("🔙 ပင်မစာမျက်နှာသို့ ပြန်ရောက်ပါပြီ။", reply_markup=reply_markup)

    # (၅) Admin တိုက်ရိုက်ဆက်သွယ်ရန် ခလုတ်နှိပ်လျှင်
    elif user_text == "👨‍💻 Admin တိုက်ရိုက်ဆက်သွယ်ရန်":
        admin_text = (
            "👨‍💻 **Admin ဆက်သွယ်ရန်**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "အောက်ပါ သင့်အကောင့် Link ပြာလေးကို နှိပ်ပြီး တိုက်ရိုက် လာရောက် ဆက်သွယ်နိုင်ပါပြီရှင် -\n\n"
            "👉 ချက်တင်ဘောက်စ်သို့ သွားရန် - @ksonegyi333"
        )
        await update.message.reply_text(admin_text)

    # (၆) ဝယ်သူက Game ID သို့မဟုတ် အခြားစာများ လာရိုက်ပို့လျှင်
    else:
        try:
            forward_text = (
                "🆔 ဝယ်သူထံမှ အချက်အလက်/စာ ရောက်ရှိလာပါသည်\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 ဝယ်သူ: {user.full_name} ({username_display})\n"
                f"💬 ပို့လိုက်သောစာ: {user_text}"
            )
            await context.bot.send_message(chat_id=ADMIN_ID, text=forward_text)
            await update.message.reply_text("🙏 အချက်အလက်များကို မှတ်တမ်းတင်ပြီးပါပြီ။ ခေတ္တစောင့်ဆိုင်းပေးပါရန်။")
        except: pass

# ဝယ်သူဘက်က ပြေစာပုံ ပို့လာပါက သင့်ထံ လှမ်းပို့မည့် စနစ်
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    photo_file = update.message.photo[-1].file_id 
    caption_text = update.message.caption if update.message.caption else ""
    username_display = f"@{user.username}" if user.username else "@None"

    buyer_info = (
        "📩 **ဝယ်သူထံမှ ပြေစာအသစ် ရောက်ရှိလာပါသည်** 📩\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 **အမည်:** {user.full_name}\n"
        f"🆔 Username: {username_display}\n"
        f"📝 ရေးလာသောစာ: {caption_text}"
    )
    try:
        await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo_file, caption=buyer_info)
        
        reply_message = (
            "✅ သင့်ရဲ့ ပြေစာပုံကို လက်ခံရရှိပါပြီ။ Admin မှ စစ်ဆေးပြီး ထည့်သွင်းပေးပါမည်။\n\n"
            "🆔 **လူကြီးမင်း၏ Game ID နှင့် Zone ID ကို ဤနေရာတွင် ရိုက်ပို့ပေးပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။**\n"
            "💡 _(ဥပမာ - 12345678 (1234))_"
        )
        await update.message.reply_text(reply_message, parse_mode="Markdown")
    except Exception as e:
        print(f"Photo Error: {e}")

def main():
    # Flask keep_alive ကို Background တွင် စတင် run ပေးခြင်း
    keep_alive()

    application = Application.builder().token("8823110888:AAEZe7k0IAaZUrzF4GNHBJUIah1TpDMqNGM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running successfully with Direct Text Mention and Flask Web Service...")
    application.run_polling()

if __name__ == "__main__":
    main()
