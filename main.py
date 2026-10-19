import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

ADMIN_ID = "7303908979"
TOKEN = "8823110888:AAEZe7k0IAaZUrzF4GNHBJUIah1TpDMqNGM"

# /start command ပို့သည့်အခါ အောက်ခြေခလုတ်များပြသခြင်း
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        ["💎 Diamond ဝယ်မည်"],
        ["📖 ဈေးဝယ်နည်းလမ်း"],
        ["📞 ဆက်သွယ်ရန်"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    welcome_text = (
        f"မင်္ဂလာပါ {user.first_name} ✨\n\n"
        "မြန်မာနိုင်ငံအတွက် Mobile Legends Diamond များကို စိတ်ချယုံကြည်စွာ ဝယ်ယူနိုင်သော စတိုးဆိုင်မှ ကြိုဆိုပါတယ်။"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# စာများနှင့် အောက်ခြေခလုတ်များကို ကိုင်တွယ်မည့်စနစ်
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_text = update.message.text
    username_display = f"@{user.username}" if user.username else "@None"

    if user_text == "💎 Diamond ဝယ်မည်":
        price_text = (
            "🔮 Weekly Pass - 9,000 ks\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 Dia 86     -  6,000ks\n"
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
            "💎 50 + 50     =  5,000ks\n"
            "💎 150 + 150   =  13,000ks\n"
            "💎 250 + 250   =  19,500ks\n"
            "💎 500 + 500   =  39,500ks\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Payment: KBZ Pay / Wave Pay\n"
            "📞 09967120289 Pyae Sone\n\n"
            "📸 _ငွေလွှဲပြီးပါက ပြေစာ Screenshot ပုံကို ဤ Bot ထဲသို့ တိုက်ရိုက် ပုံရိုက်ပို့ပေးနိုင်ပါသည်_"
        )
        buy_keyboard = [
            ["💎 86 Dia (6,000 ks)", "💎 172 Dia (12,000 ks)"],
            ["💎 257 Dia (18,000 ks)", "💎 344 Dia (24,000 ks)"],
            ["🔮 Weekly Pass (9,000 ks)"],
            ["⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်"]
        ]
        reply_markup = ReplyKeyboardMarkup(buy_keyboard, resize_keyboard=True)
        await update.message.reply_text(price_text, reply_markup=reply_markup, parse_mode="Markdown")

    elif user_text == "📖 ဈေးဝယ်နည်းလမ်း":
        guide_text = (
            "📖 **ဈေးဝယ်ယူရန် နည်းလမ်းများ**\n\n"
            "၁။ လိုချင်သော Diamond ပမာဏကို ရွေးချယ်ပါ။\n"
            "၂။ ငွေပေးချေမှု (KBZ Pay / Wave Pay) ဖြင့် ငွေလွှဲပါ။\n"
            "၃။ ငွေလွှဲပြေစာ Screenshot နှင့် Game ID / Zone ID ကို Bot ထဲသို့ ပို့ပေးပါ။\n"
            "၄။ အတည်ပြုပြီးပါက Diamond ကို အမြန်ဆုံး ဖြည့်သွင်းပေးပါမည်။"
        )
        keyboard = [["⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(guide_text, reply_markup=reply_markup, parse_mode="Markdown")

    elif user_text == "📞 ဆက်သွယ်ရန်":
        contact_text = (
            "📞 **ဆက်သွယ်ရန်**\n\n"
            "အရေးပေါ်ဆက်သွယ်ရန် Admin: @ksonegyi333 သို့ တိုက်ရိုက် ဆက်သွယ်နိုင်ပါသည်။"
        )
        keyboard = [["⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(contact_text, reply_markup=reply_markup, parse_mode="Markdown")

    elif user_text == "⬅️ ပင်မစာမျက်နှာသို့ ပြန်ရန်":
        keyboard = [
            ["💎 Diamond ဝယ်မည်"],
            ["📖 ဈေးဝယ်နည်းလမ်း"],
            ["📞 ဆက်သွယ်ရန်"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("🔙 ပင်မစာမျက်နှာသို့ ပြန်ရောက်ပါပြီ။", reply_markup=reply_markup)

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
            await context.bot.send_message(chat_id=ADMIN_ID, text=alert_selection, parse_mode="Markdown")
        except: pass

    else:
        try:
            forward_text = (
                "🆔 **ဝယ်သူထံမှ အချက်အလက်/စာ ရောက်ရှိလာပါသည်**\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 ဝယ်သူ: {user.full_name} ({username_display})\n"
                f"💬 ပို့လိုက်သောစာ: {user_text}"
            )
            await context.bot.send_message(chat_id=ADMIN_ID, text=forward_text, parse_mode="Markdown")
            await update.message.reply_text("🙏 အချက်အလက်များကို လက်ခံရရှိပါပြီ။ Admin မှ စစ်ဆေးပြီး ဆောင်ရွက်ပေးပါမည်။")
        except: pass

# ပုံ (Screenshot) ပို့လာပါက လက်ခံမည့်စနစ်
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
        await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo_file, caption=buyer_info, parse_mode="Markdown")
        reply_message = (
            f"✅ သင့်ရဲ့ ပြေစာပုံကို လက်ခံရရှိပါပြီ[span_0](start_span)[span_0](end_span)။\n\n"
            "🆔 **လူကြီးမင်း၏ Game ID နှင့် Zone ID ကို ဤနေရာတွင် ဆက်လက်ရိုက်ပို့ပေးပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။**"
        )
        await update.message.reply_text(reply_message, parse_mode="Markdown")
    except Exception as e:
        print(f"Photo Error: {e}")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Store Bot with ReplyKeyboard is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
