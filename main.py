from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Start Command အတွက် Function
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

# ပွဲစဉ်များ ပြပေးသည့် Function
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        await query.edit_message_caption(caption="⚽ ဒီနေ့ပွဲစဉ်များ:\n1. Man Utd vs Liverpool\n2. Real Madrid vs Barca")

if __name__ == '__main__':
    # သင့် Token ကို ဒီနေရာမှာ ထည့်ပါ
    app = ApplicationBuilder().token("8897020821:AAFYPCopRI84EzIK5GstAM99Edo5Pz0Sq18").build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    app.run_polling()
