import os
import logging
from telethon import TelegramClient, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.stories import GetPeerStoriesRequest

API_ID = 34368306
API_HASH = '647e6ff145a16cb6b0fb12777e512e63'

client = TelegramClient('my_story_user_session', API_ID, API_HASH)

os.makedirs('./downloaded_story', exist_ok=True)
os.makedirs('./downloaded_posts/videos', exist_ok=True)
os.makedirs('./downloaded_posts/photos', exist_ok=True)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "မင်္ဂလာပါ!\n"
        "- Story များကို Stealth Mode (သူများမသိအောင်) ကြည့်ရန်: `/story @username` ဟု ပို့ပါ။\n"
        "- ပို့စ်လင့်ခ်ဖြင့် ဒေါင်းလုပ်ဆွဲရန်: Link ကို တိုက်ရိုက်ပို့ပါ။"
    )

# Story ကို Stealth Mode (အမည်မဖော်ဘဲ/View မတက်ဘဲ) ဖြင့် ကြည့်ရှုဒေါင်းလုပ်ဆွဲမည့် Command
@client.on(events.NewMessage(pattern=r'/story\s+(@\w+)'))
async def download_story_stealth(event):
    username = event.pattern_match.group(1).lstrip('@')
    await event.respond(f"@{username} ရဲ့ Story များကို Stealth Mode ဖြင့် ရှာဖွေနေပါပြီ...")
    
    try:
        result = await client(ResolveUsernameRequest(username=username))
        user = result.users[0]
        
        # Story များကို ဆွဲထုတ်ခြင်း (Read API ကို ခေါ်ဆိုခြင်း မရှိပါ)
        stories = await client(GetPeerStoriesRequest(peer=user))
        
        if not stories.stories.stories:
            await event.respond(f"ယခုလက်ရှိ @{username} တွင် ကြည့်ရှုနိုင်သော Story မရှိပါ။")
            return
            
        count = 0
        for story in stories.stories.stories:
            if story.media:
                path = await client.download_media(story.media, file='./downloaded_story/')
                if path:
                    count += 1
                    await client.send_file(
                        event.chat_id, 
                        path, 
                        caption=f"Stealth Story from @{username}"
                    )
                    
        if count == 0:
            await event.respond("ဒေါင်းလုပ်ဆွဲ၍ရသော Story မီဒီယာ မတွေ့ပါ။")
        else:
            await event.respond(f"အောင်မြင်ပါပြီ! Story {count} ခုကို တစ်ဖက်လူ မသိစေဘဲ (Stealth ဖြင့်) ဒေါင်းလုပ်ဆွဲပြီးပါပြီ။")
            
    except Exception as e:
        await event.respond(f"အမှားအယွင်း ဖြစ်ပေါ်သည်: {e}")

# လင့်ခ်ဖြင့် ပို့စ်များ/ဗီဒီယိုများ ဒေါင်းလုပ်ဆွဲမည့် Command
@client.on(events.NewMessage(pattern=r'(https?://t\.me/[^\s]+)'))
async def download_by_link(event):
    link = event.pattern_match.group(1)
    await event.respond("ပေးပို့ထားသော လင့်ခ်မှ မီဒီယာများကို ရှာဖွေနေပါပြီ...")
    
    try:
        parts = link.split('/')
        msg_id = int(parts[-1])
        
        if 'c' in parts:
            chat_id = int('-100' + parts[-2])
            target = await client.get_entity(chat_id)
        else:
            username = parts[-2]
            target = await client.get_entity(username)
            
        message = await client.get_messages(target, ids=msg_id)
        
        if message and message.media:
            is_video = message.video or (message.document and message.document.mime_type.startswith('video'))
            target_folder = './downloaded_posts/videos/' if is_video else './downloaded_posts/photos/'
            
            path = await client.download_media(message, file=target_folder)
            if path:
                if message.text:
                    txt_path = f"{path}.txt"
                    with open(txt_path, 'w', encoding='utf-8') as f:
                        f.write(message.text)
                
                await client.send_file(
                    event.chat_id, 
                    path, 
                    caption=message.text or "Downloaded Media Post"
                )
                await event.respond("အောင်မြင်ပါပြီ! ဖိုင်ကို သက်ဆိုင်ရာ Folder ထဲသို့ သိမ်းဆည်းပေးပြီးပါပြီ။")
        else:
            await event.respond("အဆိုပါလင့်ခ်တွင် ဒေါင်းလုပ်လုပ်နိုင်သော မီဒီယာ မရှိပါ။")
            
    except Exception as e:
        await event.respond(f"အမှားအယွင်း ဖြစ်ပေါ်သည်: {e}")

print("Telegram Stealth Story & Link Downloader Bot စတင်နေပါပြီ...")
client.start()
client.run_until_disconnected()
