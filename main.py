async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ၁။ အရင်ဆုံး စာသားကို ပို့ပေးမယ်
    text_message = (
        "🔥 ပွဲကောင်းများ စတင်တော့မည်!\n\n"
        "✨ Area 69 မှ ကြိုဆိုပါတယ်! \n"
        "အောက်ပါ ခလုတ်များကို နှိပ်၍ ဝန်ဆောင်မှုရယူနိုင်ပါသည်။"
    )
    
    keyboard = [
        [InlineKeyboardButton("💰 ငွေသွင်း / ငွေထုတ်", url='https://t.me/kothu7877')],
        [InlineKeyboardButton("⚽ ဒီနေ့ပွဲစဉ်များ", callback_data='matches')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # စာနဲ့ ခလုတ်ကို အရင်ပို့မယ်
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=text_message, 
        reply_markup=reply_markup
    )
    
    # ၂။ ပြီးမှ ပုံကို သီးခြားပို့ပေးမယ်
    photo_url = "https://i.ibb.co/LDSGTCKD/1000032426.png" 
    await context.bot.send_photo(
        chat_id=update.effective_chat.id, 
        photo=photo_url
    )
