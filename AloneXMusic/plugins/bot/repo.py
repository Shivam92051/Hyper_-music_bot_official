from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """**
ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴋʏᴀ 😂🤡
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🍃", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/World_friend_chatting_zone"),
          InlineKeyboardButton("🥀ᴏᴡɴᴇʀ🍃", url="https://t.me/DEVELOPER_K4K4SHI"),
          ],
               [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Dil_sa_shayari"),

],
[
              InlineKeyboardButton("˹ꭑⱺⱺ𐓣 ꭙ ѕραмᴇꝛ˼", url=f"https://t.me/ANOX_SPAMBOT?startgroup=true"),
              InlineKeyboardButton("︎˹ꭑⱺⱺ𐓣 ꭙ ᴍᴜꜱɪᴄ˼", url=f"https://t.me/ANOX_MUSICBOT?startgroup=true"),
              ],
              [
              InlineKeyboardButton("ʀᴇᴘᴏ", url=f"https://telegra.ph/file/78be765f35211e764a9d5.mp4"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://r2.easyimg.io/swqqfpgqm/hw_much_u_r_grwn_thn_me.jpeg",
        caption=start_txt,
        reply_markup=reply_markup
    )
