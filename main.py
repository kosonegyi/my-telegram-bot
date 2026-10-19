import os
import asyncio
from threading import Thread
from flask import Flask
import logging
import re
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
ADMIN_ID = 7303908979 

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
    chat_id = update.message.chat_id
    
    # Admin ဘက်မှ ဝယ်သူဆီသို့ Reply ပြန်နေခြင်းဟုတ်မဟုတ် စစ်ဆေးခြင်း (ပြင်ပကြော်ငြာစာများ လုံးဝမပါစေရန် တိကျစွာ စစ်ဆေးခြင်း)
    if chat_id == ADMIN_ID and update.message.reply_to_message:
        try:
            replied_msg = update.message.reply_to_message.text or update.message.reply_to_message.caption or ""
            
            # ချက်တင်စာသားထဲမှ ဝယ်သူ၏ Telegram ID (tg://user?id=...) သို့မဟုတ် id= ကို ရှာဖွေခြင်း
            match = re.search(r'id=(\d+)', replied_msg)
            if not match:
                # Entities များထဲမှ ID ရှာဖွေခြင်း (Fallback)
                for entity in update.message.reply_to_message.entities or []:
                    if entity.url and "id=" in entity.url:
                        match = re.search(r'id=(\d+)', entity.url)
                        if match:
                            break
            
            if match:
                target_user_id = match.group(1)
                # ဝယ်သူဆီသို့ Admin ရေးလိုက်သော စာသားကိုသာ တိုက်ရိုက်ပို့မည် (ပြင်ပလင့်ခ်/ကြော်ငြာများ လုံးဝမပါစေရန်)
                await context.bot.send_message(
                    chat_id=int(target_user_id),
                    text=f"{user_text}"
                )
                await update.message.reply_text("✅ ဝယ်သူထံသို့ စာပို့ပြီးပါပြီ။")
                return
            else:
                await update.message.reply_text("❌ ဤမက်ဆေ့ပ်မှ ဝယ်သူ၏ ID ကို ရှာမတွေ့ပါ။ (ဝယ်သူ၏ မက်ဆေ့ပ်ကိုသာ Reply လုပ်ပါ)")
                return
        except Exception as e:
            await update.message.reply_text(f"❌ ပို့၍မရပါ။ Error: {e}")
            return

    # Username ရှိလျှင် @username ပြမည်၊ မရှိလျှင် Admin ဘက်မှ နှိပ်၍ တိုက်ရိုက်ဆက်သွယ်နိုင်ရန် Profile Link ချိတ်ပေးမည်
    if user.username:
        username_display = f"@{user.username}"
    else:
        username_display = f"[{user.full_name}](tg://user?id={user.id})"

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
        await update.message.reply_text(price_text, reply_markup=reply_markup, parse_mode="Markdown")
        
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID, 
                text=f"💎 Dia စျေးနှုန်းများကြည့်သူ: {user.full_name}\n👤 Username/Profile: {username_display}", 
                parse_mode="Markdown"
            )
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

    # (၃) ဝယ်သူမှ Dia ပမာဏ တစ်ခုခုကို နှိပ်လျှင်
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
            alert_selection = f"🛒 **ဝယ်ယူရန် ပမာဏရွေးချယ်မှု အသစ်**\n━━━━━━━━━━━━━━━━━━━━\n👤 ဝယ်သူ: {user.full_name}\n🔗 Profile: {username_display}\n💎 ရွေးချယ်သွားသည်: {user_text}"
            await context.bot.send_message(chat_id=ADMIN_ID, text=alert_selection, parse_mode="Markdown")
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

    # (၆) Game ID သို့မဟုတ် အခြားစာများ ပို့လာပါက Validation စစ်ဆေးခြင်း
    else:
        # Game ID ပုံစံ (ဂဏန်းသီးသန့် သို့မဟုတ် Zone ပါဝင်ခြင်း) ဟုတ်မဟုတ် စစ်ဆေးခြင်း
