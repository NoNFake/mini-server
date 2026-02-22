def coockie_to_dict(cookie_str: str) -> dict:
    cookies = {}
    for part in cookie_str.split(';'):
        part = part.strip()
        if '=' in part:
            name, value = part.split('=', 1)
            # # Декодуємо %3B -> ; та інші спецсимволи
            # cookies[name] = unquote(value)
            cookies[name] = value
    return cookies
