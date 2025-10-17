from ..usrbot import UsrBot
from pyrogram import filters, enums
from pyrogram.errors import (
    BotInlineDisabled,
    BotResponseTimeout)
from ..sample_config import Config, MessagesTag
import logging
import asyncio
import random as rnd

log = logging.getLogger(__name__)

word_trigger = (
    r"(хуй(ло|ня|чок|чик)?|хуя(чок|рик|к)?|"
    r"пизд(а|ець|єць|юк|юк)?|пздц|пзд|"
    r"єб(ать|ло|ан|уч|тво|ись)?|еб(ать|ло|ан|уч|ись)?|йоб(аний| твою)?|"
    r"бля(т|ха|ха-муха|хаха)?|"
    r"гандон(и|чик)?|през(ервати|ерватив)|"
    r"мудак(и|ів)?|"
    r"долбо(йоб|ёб|йоб|єб)?|"
    r"сука(мать|н|ни|ні)?|"
    r"шлюх(а|и|ар|ари)?|"
    r"мраз(ь|и|ота)?|"
    r"уёб(ок|ки)?|уеб(ок|ки)?|уїб(ок|ки)?|"
    r"підор(и|аси|чик)?|пiдор(и|аси)?|pidor|pidaras|"
    r"нах(уй|рін|рєн)?|nahui|"
    r"залуп(а|и)?|залуп(к|оньк)?|"
    r"курва(и|ти)?|"
    r"сра(ка|ний|ти|ння)?)"
)
cenc = "*"

@UsrBot.on_message(
    (filters.me | filters.private) & filters.regex(word_trigger) 
)


def censor_tetx(text: str) -> str:
    ...

async def ban_words(client, message):
    try:
        chat_id = message.chat.id
        text_ed = message.text

        log.info(f"word_trigger: {word_trigger}")
        text_ed = text_ed.replace(rnd.choice(text_ed), cenc)

        await client.edit_message_text(
                chat_id=chat_id,
                message_id=message.id,
                text=f"{text_ed}"
            )

    except Exception as e:
        # await message.reply_text(MessagesTag.msg_fail)
        # await message.reply_text(f'''{MessagesTag.tiktok_tag}\n```{Config.gen_cats()}{Config.tiktok_reply()}```''')
        # log.error(f"Error: {e}")
        return


