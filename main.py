from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ပုံ Link ကို သုံးပြီး စတင်တဲ့ Function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # သင်ရထားတဲ့ Direct Link
    photo_url = "https://i.ibb.co/LDSGTCKD/1000032426.png" 
    
    keyboard = [
        [InlineKeyboardButton("💰 ငွေသွင်း / ငွေထုတ်", url='https://t.me/kothu7877')],
        [InlineKeyboardButton("⚽ ဒီနေ့ပွဲစဉ်များ", callback_data='matches')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # ပုံနဲ့အတူ ခလုတ်များကို ပို့ပေးခြင်း
    await context.bot.send_photo(
        chat_id=update.effective_chat.id, 
        photo=photo_url, 
        caption="✨ Area 69 မှ ကြိုဆိုပါတယ်! \nအောက်ပါ ခလုတ်များကို နှိပ်၍ ဝန်ဆောင်မှုရယူနိုင်ပါသည်။",
        reply_markup=reply_markup
    )

# ပွဲစဉ်များ ပြပေးသည့် Function
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'matches':
        await query.edit_message_caption(caption="⚽ ဒီနေ့ပွဲစဉ်များ:\n1. Man Utd vs Liverpool\n2. Real Madrid vs Barca")

if __name__ == '__main__':
    # သင်ပေးလိုက်တဲ့ Token ကို ဒီနေရာမှာ ထည့်ပေးလိုက်ပါပြီ
    app = ApplicationBuilder().token("8897020821:AAFYPCopRI84EzIK5GstAM99Edo5Pz0Sq18").build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    app.run_polling()
