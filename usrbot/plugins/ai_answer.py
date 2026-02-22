__command__ = ".ai_answer"
__info__ = ".ai_answer - on/off, .ai_answer add/del [id]"

import asyncio
from hydrogram import filters
from ..usrbot import UsrBot
from ..usrbot import Config
import os
import random as rnd
import aiosqlite


from .core.src.gen_text import generate_text
from .core.src.prompt import prompt_yurii


import logging
log = logging.getLogger(__name__)

MEMMORIES_DB = 'memmories.db'
AI_ENABLED = True
user_contexts = {}



async def init_db():
    async with aiosqlite.connect(MEMMORIES_DB) as db:
        # История сообщений
        await db.execute('''CREATE TABLE IF NOT EXISTS history 
            (user_id INTEGER, role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        # Белый список юзеров
        await db.execute('''CREATE TABLE IF NOT EXISTS allowed_users (user_id INTEGER PRIMARY KEY)''')
        await db.commit()



async def is_user_allowed(user_id: int) -> bool:
    async with aiosqlite.connect(MEMMORIES_DB) as db:
        async with db.execute('SELECT 1 FROM allowed_users WHERE user_id = ?', (user_id,)) as cur:
            return await cur.fetchone() is not None


async def add_user(user_id: int):
    async with aiosqlite.connect(MEMMORIES_DB) as db:
        await db.execute('INSERT OR IGNORE INTO allowed_users (user_id) VALUES (?)', (user_id,))
        await db.commit()

async def del_user(user_id: int):
    async with aiosqlite.connect(MEMMORIES_DB) as db:
        await db.execute('DELETE FROM allowed_users WHERE user_id = ?', (user_id,))
        await db.commit()




async def memmories(user_id: int, new_message = None, bot_answer = None) -> str:
    async with aiosqlite.connect(MEMMORIES_DB) as db:
        if new_message:
            await db.execute('INSERT INTO history (user_id, role, content) VALUES (?, ?, ?)', (user_id, "user", new_message))
        if bot_answer:
            await db.execute('INSERT INTO history (user_id, role, content) VALUES (?, ?, ?)', (user_id, "assistant", bot_answer))
        await db.commit()
        async with db.execute('SELECT role, content FROM history WHERE user_id = ? ORDER BY timestamp DESC LIMIT 20', (user_id,)) as cur:
            rows = await cur.fetchall()
            return "\n".join([f"{r[0]}: {r[1]}" for r in reversed(rows)])



async def proccess_batch(chat_id: int, client: UsrBot):
    data = user_contexts[chat_id]
    full_text = " ".join(data["messages"])
    data["messages"], data["task"] = [], None


    try:
    
        from hydrogram.enums import ChatAction
        await client.send_chat_action(chat_id, ChatAction.TYPING)
        
        history = await memmories(chat_id, new_message=full_text)
        user_input = " ".join(prompt_yurii(text=full_text, history_text=history).split())
        reply = await generate_text(user_input)
        
        if reply:
            clean_reply = reply.replace("**", "").replace("###", "").strip()
            await memmories(chat_id, bot_answer=clean_reply)
            await client.send_message(chat_id, clean_reply)
            
    except Exception as e:
        log.error(f"Error in processing batch: {e}")



@UsrBot.on_message(filters.me & filters.command("ai_answer", prefixes="."))
async def ai_cmd_handler(client, message):
    global AI_ENABLED
    args = message.command[1:]

    if not args:
        AI_ENABLED = not AI_ENABLED
        status = "ON" if AI_ENABLED else "OFF"
        return await message.edit_text(f"<b>nn_yurii {status}</b>")

    action = args[0].lower()
    
    if action == "add" and len(args) > 1:
        uid = int(args[1])
        await add_user(uid)
        await message.edit_text(f"<b>✅ user {uid} add.</b>")
    
    elif action == "del" and len(args) > 1:
        uid = int(args[1])
        await del_user(uid)
        await message.edit_text(f"<b>❌ user {uid} del.</b>")
 


@UsrBot.on_message(filters.incoming & ~filters.me)
async def ai_auto_responder(client, message):
    if not AI_ENABLED:
        return

    chat_id = message.chat.id
    if not await is_user_allowed(chat_id):
        return
    
    print(f"[{chat_id}]: {message}")


    if chat_id not in user_contexts:
        user_contexts[chat_id] = {"messages": [], "task": None}


    user_contexts[chat_id]["messages"].append(message.text or "")

    if user_contexts[chat_id]["task"]:
        user_contexts[chat_id]["task"].cancel()


    async def waiter():
        try:
            await asyncio.sleep(rnd.randint(10, 15))
            await proccess_batch(chat_id, client)
        except asyncio.CancelledError: pass
    user_contexts[chat_id]["task"] = asyncio.create_task(waiter())



asyncio.ensure_future(init_db())
