import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

ADMIN_ID = "7303908979"
TOKEN = "8823110888:AAEZe7k0IAaZUrzF4GNHBJUIah1TpDMqNGM"

# /start command ပို့သည့်အခါ Inline ခလုတ်များဖြင့် ပြသခြင်း
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

# ခလုတ်များကို နှိပ်သည့်အခါ ကိုင်တွယ်မည့်စနစ်
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "buy_diamond":
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
            "📸 _ငွေလွှဲပြီးပါက ပြေစာ Screenshot ပုံကို ဤ Bot ထဲသို့ တိုက်ရိုက် ပုံရိုက်ပို့ပေးနိုင်ပါသည်_\n\n"
            "🆔 **ကျေးဇူးပြု၍ ဝယ်ယူလိုသော Game ID နှင့် Zone ID ကို ပေးပို့ပါ။**"
        )
        await query.message.edit_text(price_text, parse_mode="Markdown")
        
    elif query.data == "guide":
        guide_text = (
            "📖 **ဈေးဝယ်ယူရန် နည်းလမ်းများ**\n\n"
            "၁။ လိုချင်သော Diamond ပမာဏကို ရွေးချယ်ပါ။\n"
            "၂။ ငွေပေးချေမှု (KBZ Pay / Wave Pay) ဖြင့် လွှဲပြងပာပါ။\n"
            "၃။ ငွေလွှဲပြေစာ Screenshot နှင့် Game ID / Zone ID ကို Bot ထဲသို့ ပို့ပေးပါ။\n"
            "၄။ အတည်ပြုပြီးပါက Diamond ကို အမြန်ဆုံး ဖြည့်သွင်းပေးပါမည်။"
        )
        keyboard = [[InlineKeyboardButton("🔙 უკანသို့", callback_data="back_home")]]
        await query.message.edit_text(guide_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif query.data == "contact":
        contact_text = (
            "📞 **ဆက်သွယ်ရန်**\n\n"
            "အရေးပေါ်ဆက်သွယ်ရန် Admin: @ksonegyi333 သို့ တိုက်ရိုက် ဆက်သွယ်နိုင်ပါသည်။"
        )
        keyboard = [[InlineKeyboardButton("🔙 უკანသို့", callback_data="back_home")]]
        await query.message.edit_text(contact_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif query.data == "back_home":
        keyboard = [
            [InlineKeyboardButton("💎 Diamond ဝယ်မည်", callback_data="buy_diamond")],
            [InlineKeyboardButton("📖 ဈေးဝယ်နည်းလမ်း", callback_data="guide")],
            [InlineKeyboardButton("📞 ဆက်သွယ်ရန်", callback_data="contact")]
        ]
        welcome_text = "မင်္ဂလာပါ ✨\n\nမြန်မာနိုင်ငံအတွက် Mobile Legends Diamond များကို စိတ်ချယုံကြည်စွာ ဝယ်ယူနိုင်သော စတိုးဆိုင်မှ ကြိုဆိုပါတယ်။"
        await query.message.edit_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard))

# ဝယ်သူမှ စာ သို့မဟုတ် Game ID ပို့လာပါက Admin ဆီသို့ ပို့ပေးမည့်စနစ်
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_text = update.message.text
    username_display = f"@{user.username}" if user.username else "@None"

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
            "✅ သင့်ရဲ့ ပြေစာပုံကို လက်ခံရရှိပါပြီ[span_2](start_span)[span_2](end_span)。\n\n"
            "🆔 **လူကြီးမင်း၏ Game ID နှင့် Zone ID ကို ဤနေရာတွင် ဆက်လက်ရိုက်ပို့ပေးပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။**"
        )
        await update.message.reply_text(reply_message, parse_mode="Markdown")
    except Exception as e:
        print(f"Photo Error: {e}")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Store Bot is running smoothly...")
    application.run_polling()

if __name__ == "__main__":
    main()
