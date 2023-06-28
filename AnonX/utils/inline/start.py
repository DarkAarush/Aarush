from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⇍𝐀ᑯᑯ 𝐢 𝐇𝖾𝐚𝐫𝗍 𝚰𐓣 𝐆𝗋ⱺυρ⇏",
                url=f"https://t.me/JiosaavnTetrisbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❁══╡𝐇𝖾ᥣρ╞══❁",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⇍𝐀ᑯᑯ 𝐢 𝐇𝖾𝐚𝐫𝗍 𝚰𐓣 𝐆𝗋ⱺυρ⇏",
                url=f"https://t.me/JiosaavnTetrisbot?startgroup=true",
            )
        ],

        
        [
        
            InlineKeyboardButton(
                text="❁══╡𝐒ⱺυ𝗋𝖼𝖾╞══❁", url=f"https://www.jiosaavn.com/"
            )
        ],

        
        [
        
            InlineKeyboardButton(
                text="❁══╡𝐂ⱺ𐓣𝗍𝖾𐓣𝗍╞══❁", url=f"https://www.jiosaavn.com/"
            )
        ],
        [
            InlineKeyboardButton(
                text="❁══╡𝐇𝖾ᥣρ╞══❁", callback_data="settings_back_helper"
            )
        ], 
     ]
    return buttons

