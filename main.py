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
USERS_FILE = "users.txt"
PREDICTIONS_FILE = "predictions.txt"  # ခန့်မှန်းချက်များ မှတ်ရန်ဖိုင်

# --- Data သိမ်းဆည်းသည့် စနစ်များ ---
def save_user(user_id):
    user_ids = set()
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            user_ids = set(f.read().splitlines())
    if str(user_id) not in user_ids:
        with open(USERS_FILE, "a") as f:
            f.write(f"{user_id}\n")

def get_all_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return f.read().splitlines()
    return []

def save_prediction(user_id, username, choice):
    # လူတစ်ယောက် တစ်ကြိမ်ပဲ ခန့်မှန်းနိုင်အောင် စစ်ဆေးမည်
    predictions = {}
    if os.path.exists(PREDICTIONS_FILE):
        with open(PREDICTIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "," in line:
                    uid, uname, ch = line.strip().split(",", 2)
                    predictions[uid] = (uname, ch)
    
    predictions[str(user_id)] = (username or "No_Username", choice)
    
    with open(PREDICTIONS_FILE, "w", encoding="utf-8") as f:
        for uid, (uname, ch) in predictions.items():
            f.write(f"{uid},{uname},{ch}\n")

# ပွဲစဉ်စာသားကို ဖတ်ခြင်း
def get_matches_text():
    if os.path.exists(MATCHES_FILE):
        with open(MATCHES_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return content if content else " လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"
    return " လက်ရှိပွဲစဉ်များ မရှိသေးပါ။"

# Admin က ပွဲစဉ်ပြင်ခြင်း
async def update_matches(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text(" သင်သည် Admin မဟုတ်ပါ။")
        return

    new_text = " ".join(context.args)
    if not new_text:
        await update.message.reply_text("စာသားထည့်ရန်လိုအပ်ပါသည်။ ဥပမာ - /update_matches  မန်ယူ vs လီဗာပူး")
        return
    
    # ပွဲစဉ်သစ်တင်တိုင်း ခန့်မှန်းချက်အဟောင်းများကို ဖျက်ပစ်မည်
    if os.path.exists(PREDICTIONS_FILE):
        os.remove(PREDICTIONS_FILE)

    with open(MATCHES_FILE, "w", encoding="utf-8") as f:
        f.write(new_text)
    await update.message.reply_text(" ပွဲစဉ်များ ပြင်ဆင်ပြီးပါပြီ။ ခန့်မှန်းချက်မှတ်တမ်းများကို Reset ပြုလုပ်ပြီးပါပြီ။")

# --- Admin က ခန့်မှန်းသူများစာရင်း ကြည့်ခြင်းစနစ် ---
async def view_predictions(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text(" သင်သည် Admin မဟုတ်ပါ။")
        return

    if not os.path.exists(PREDICTIONS_FILE) or os.path.getsize(PREDICTIONS_FILE) == 0:
        await update.message.reply_text(" လက်ရှိတွင် လာရောက်ခန့်မှန်းထားသူ မရှိသေးပါ။")
        return

    text = " <b>ပွဲစဉ်ခန့်မှန်းထားသူများ စာရင်း</b>\n\n"
    with open(PREDICTIONS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "," in line:
                uid, uname, ch = line.strip().split(",", 2)
                text += f" @{uname} ({uid}) -> <b>{ch}</b>\n"
                
    await update.message.reply_text(text, parse_mode='HTML')

# --- အလိုအလျောက် ပွဲစဉ်သတိပေးချက်စနစ် ---
async def remind_match(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text(" သင်သည် Admin မဟုတ်ပါ။")
        return
    if len(context.args) < 2:
        await update.message.reply_text(" ပုံစံ - /remind_match [မိနစ်] [စာသား]")
        return
    try:
        minutes = int(context.args[0])
        reminder_text = " ".join(context.args[1:])
    except ValueError:
        await update.message.reply_text(" မိနစ်နေရာတွင် ဂဏန်းထည့်ပါ။")
        return

    await update.message.reply_text(f" နောက်ထပ် {minutes} မိနစ်အကြာတွင် သတိပေးစာ ပို့ပေးပါမည်။")
    await asyncio.sleep(minutes * 60)

    users = get_all_users()
    success_count = 0
    full_message = f" <b>[ပွဲကြိုသတိပေးချက်]</b>\n\n{reminder_text}"
    keyboard = [[InlineKeyboardButton(" ပွဲစဉ်ကြည့်ရန်", callback_data='matches')]]

    for user_id in users:
        try:
            await context.bot.send_message(chat_id=int(user_id), text=full_message, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
            success_count += 1
            await asyncio.sleep(0.05)
        except Exception:
            continue
    await context.bot.send_message(chat_id=ADMIN_ID, text=f" ပွဲကြိုသတိပေးချက်ကို လူဦးရေ {success_count} ယောက်ဆီ ပို့ပြီးပါပြီ။")

# မူလ Function များ
def get_main_text():
    return (
        " <b>ပွဲကောင်းများ စတင်တော့မည်!</b>\n\n"
        " <b>မင်္ဂလာပါ!</b> Area 69 (1xbet) မှ ကြိုဆိုပါတယ်။\n"
        "အောက်ပါခလုတ်များဖြင့် ရွေးချယ်နိုင်ပါသည်။ "
    )

def get_keyboard():
    return [
        [InlineKeyboardButton(" ဒီနေ့ပွဲစဉ်များ", callback_data='matches')],
        [InlineKeyboardButton(" ရလဒ်ခန့်မှန်းပြီး မဲနှိုက်ရန်", callback_data='predict_menu')],
        [InlineKeyboardButton(" Ngwe Thwin/Ngwe Htok", url='https://t.me')],
        [InlineKeyboardButton(" Admin ထံမှ အထူး Bonus ရယူရန်", url='https://t.me')]
    ]

async def start(update, context):
    save_user(update.message.from_user.id)
    await update.message.reply_text(get_main_text(), reply_markup=InlineKeyboardMarkup(get_keyboard()), parse_mode='HTML')

async def broadcast(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text(" သင်သည် Admin မဟုတ်ပါ။")
        return
    try:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=get_main_text(), reply_markup=InlineKeyboardMarkup(get_keyboard()), parse_mode='HTML')
        await update.message.reply_text(" Channel သို့ Broadcast လုပ်ပြီးပါပြီ။")
    except Exception as e:
        await update.message.reply_text(f" Error: {e}")

async def button_click(update, context):
    query = update.callback_query
    await query.answer()
    save_user(query.from_user.id)
    
    if query.data == 'matches':
        await query.message.edit_text(get_matches_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" နောက်သို့", callback_data='start')]]))
    
    elif query.data == 'start':
        await query.message.edit_text(get_main_text(), parse_mode='HTML', reply_markup=InlineKeyboardMarkup(get_keyboard()))
    
    # --- ရလဒ်ခန့်မှန်းခြင်း Menu ---
    elif query.data == 'predict_menu':
        p_keyboard = [
            [InlineKeyboardButton(" အိမ်ရှင်အသင်းနိုင် (Home Win)", callback_data='pred_Home')],
            [InlineKeyboardButton(" သရေကျမည် (Draw)", callback_data='pred_Draw')],
            [InlineKeyboardButton(" ဧည့်သည်အသင်းနိုင် (Away Win)", callback_data='pred_Away')],
            [InlineKeyboardButton(" နောက်သို့", callback_data='start')]
        ]
        p_text = " <b>ဒီနေ့ပွဲစဉ်အတွက် ဘယ်ရလဒ် ထွက်လာမလဲ ခန့်မှန်းပေးပါ။</b>\n\nမှန်ကန်အောင် ခန့်မှန်းနိုင်သူများကို Admin မှ အထူး Bonus မဲနှိုက်ပေးမည် ဖြစ်သည်။"
        await query.message.edit_text(p_text, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(p_keyboard))
    
    elif query.data.startswith('pred_'):
        choice = query.data.split('_')[1]
        save_prediction(query.from_user.id, query.from_user.username, choice)
        
        reply_keyboard = [[InlineKeyboardButton(" ပင်မမီနူးသို့", callback_data='start')]]
        await query.message.edit_text(f" သင်၏ ခန့်မှန်းချက် (<b>{choice}</b>) ကို စနစ်ထဲသို့ မှတ်သားပြီးပါပြီ။\n\nပွဲပြီးဆုံးပါက Admin မှ အနိုင်ရသူများကို ဆက်သွယ်ပေးပါမည်။", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(reply_keyboard))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("update_matches", update_matches))
    app.add_handler(CommandHandler("remind_match", remind_match))
    app.add_handler(CommandHandler("view_predictions", view_predictions)) # ခန့်မှန်းချက်ကြည့်ရန် Command အသစ်
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot စတင်နေပါပြီ...")
    app.run_polling()
