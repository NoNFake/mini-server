from rich import print, traceback
traceback.install()
import asyncio
import json

import aiohttp
import re


from .streamGenarte import encode_message
from .genHeadres import get_headers
from .getCookie import coockie_to_dict
import sys

class AI:
    def __init__(self, session: aiohttp.ClientSession, cookie: dict, name: str, text: str):
        self.session = session
        self.cookie = cookie
        self.name = name
        self.text = text
        self.headers = get_headers()
        
        #self.url = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate?bl=boq_assistant-bard-web-server_20260128.03_p2&f.sid=3599017720615996060&hl=ru&_reqid=14738471&rt=c"
        self.url = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate?bl=boq_assistant-bard-web-server_20260108.03_p1&f.sid=5962932720473195260&hl=fr&_reqid=44140510&rt=c"
        #self.url = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate?bl=boq_assistant-bard-web-server_20251125.06_p0&f.sid=1640004648564881796&hl=uk&_reqid=2654386&rt=c"
        #self.url = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate?bl=boq_assistant-bard-web-server_20251217.07_p5&f.sid=-1856301012504386847&hl=ru&_reqid=5335622&rt=c"

        


    async def send_request(self, file_data=None, file_name=None, content_type=None):
        
        file_info = None
        
        # 1. Если передан файл, сначала загружаем его
        if file_data:
            print(f"Загрузка файла {file_name}...")
            resource_id = await upload_file(self.session, file_data, file_name, content_type)
            if resource_id:
                print(f"Файл загружен: {resource_id}")
                file_info = {
                    "url": resource_id,
                    "name": file_name,
                    "type": content_type
                }
            else:
                print("[red]Не удалось загрузить файл, отправляю только текст[/red]")

        # 2. Кодируем сообщение (с файлом или без)
        encoded_body = encode_message(self.text)
        payload = f"f.req={encoded_body}"
        
        async with self.session.post(
            url=self.url,
            data=payload,
        ) as resp:
            if resp.status != 200:
                return None
            response_text = await resp.text()
            return response_text


# encode_message = encoder_mess("Ок")
def clean_google_stream(raw_text):
    json_objects = []
    lines = raw_text.split('\n')
    buffer = ""
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        if re.match(r'^\d+$', line):
            continue
            
        buffer += line
        
        try:
            obj = json.loads(buffer)
            json_objects.append(obj)
            buffer = ""
        except json.JSONDecodeError:
            continue
            
    return json_objects


def extract_body(raw_text):
    if raw_text.startswith(")]}'"):
        raw_text = raw_text.replace(")]}'", "", 1).strip()


    chunks = re.findall(r'\[\["wrb\.fr".+?\]\](?=\n\d+\n|\]$|$)', raw_text, re.DOTALL)
    
    final_text = ""

    for chunk in chunks:
        try:
            data = json.loads(chunk)
            inner_json_str = data[0][2]
            if not inner_json_str:
                continue
                
            inner_data = json.loads(inner_json_str)
            
            if len(inner_data) > 4 and inner_data[4]:
                parts = inner_data[4][0][1]
                if parts:
                    current_text = "".join(parts)
                    if len(current_text) > len(final_text):
                        final_text = current_text
        except (json.JSONDecodeError, IndexError, TypeError):
            continue
            
    return final_text.replace('\\n', '\n') 


async def main(text: str, file_bytes: bytes = None, file_name: str = None, mime_type: str = None):
    with open("cookie.txt", "r") as f:
        cookie_str = f.read().strip()
    cookie_dict = coockie_to_dict(cookie_str)
    header = get_headers()

    async with aiohttp.ClientSession(cookies=cookie_dict, headers=header) as session:
        bot = AI(session, cookie_dict, "Bot_1", text)
        # Передаем файл в send_request
        response = await bot.send_request(file_bytes, file_name, mime_type)
        return response





async def generate_text(text: str, file_path: str = None) -> str:
    """
    Теперь принимает опциональный путь к файлу
    """
    file_bytes = None
    file_name = None
    mime_type = None

    if file_path:
        file_name = file_path.split("/")[-1]
        # Простое определение типа
        if file_name.endswith(".ogg"): mime_type = "audio/ogg"
        elif file_name.endswith(".mp3"): mime_type = "audio/mpeg"
        elif file_name.endswith(".jpg"): mime_type = "image/jpeg"
        elif file_name.endswith(".png"): mime_type = "image/png"
        
        with open(file_path, "rb") as f:
            file_bytes = f.read()

    result = await main(text, file_bytes, file_name, mime_type)
    
    if result:
        # Нужно импортировать extract_body из того же файла или как у вас устроено
        from .gen_text import extract_body 
        clean_text = extract_body(result)
        return clean_text
    return ""
