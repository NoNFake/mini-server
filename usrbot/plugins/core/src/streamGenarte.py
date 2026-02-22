import urllib.parse
import json
from rich import print 
from enum import Enum
"""
Поле,Значение/Тип,Описание
Payload, Hello how are u???,Входящий текст пользователя.
Language,en-US,Код языка для обработки.
Session ID,c_f8a53...,Идентификатор сеанса связи.
Request Token,AwAAAA... (Base64),Зашифрованные данные о состоянии сессии.
Device ID,5422118A-...,Уникальный ID вашего устройства/браузера.
Model Config,"[4], [2], [1]",Внутренние индексы для выбора алгоритма обработки.

"""


class ModelConfig(Enum):
    ARCHITECTURE_VERSION:   int = 5 
    RESPONSE_MODE:          int= 6
    PROCESSING_TIER:        int = 7


def encode_message(text: str) -> str:

    model_cfg = ModelConfig
    version = model_cfg.ARCHITECTURE_VERSION.value
    mode    = model_cfg.RESPONSE_MODE.value
    tier    = model_cfg.PROCESSING_TIER.value

    json_text: str = json.dumps(text.replace('"', '').replace("'", "").replace("[", "").replace("]", "").replace("**", "").replace("###", ""). replace("{", "").replace("}",""))

    inner_text: str = json_text[1:-1]
    text_encode: str = urllib.parse.quote(inner_text)

    lang:  str = "en-US" 
    token: str = "AwAAAAAAAAAQwBHO-LzoF6Ltom6VrRk%5C%22%5D%2C%5C%22!0NOl04vNAAb9MTdP3TFCF0zkkdXNPz47ADQBEArZ1B51v3wSb4thPSxNi-NTciJ66RX1QVNZgqcQZyoSsshlqJFCIIpBFl83KDJlLztXAgAAAFpSAAAAA2gBB34AQWIK_v0YSUap_CQCtjSgGXUV0yrCFDIL1jheijeZ1_Bo-L4AMCimlQBsfE2gMfRM5kTdvvu_B8wnAFTi4guRSQFvmQNow-8R9DDs4KODLVJE62mRZ0uYlT1l5i0G0k2R3XU5lSz7KlKz7Jy7rkOA2AfapXGXxkItpnmMNdq9-VKqRhuIQ2xXGRzfi7SSU4-k2wm3oQGhFvzQyTTRkEiWL2KrU3_aAsEj3wOHe600SIA5m20aKRNFpJ6jPkA-DV51mSkAO8ND_UCbkitX2DWG8ASHvzsb6kvxzfXzlC2Ik5cWF8bRtRUl4ia_NsCwJOitXZ3TSKaIOKpdgT579laRKqir-ktqJjJS5Cp12fngi9X1D73ODVujuQFzyvuzqyNkvm0n7l67fX-I7Pxg04jDLBYTYW4iqojdVxGvyvIkvY5FaLlp1SEsfg-JLp35MqpVTuaskLV_e6Q3bX0Ng9y_HfvMJU6AgxSRCPrPegq87bkaoJGXali_XT-SwW2TxW5XjFrvN0RmEYqlYmQ8UF0exBM-5SyXox5OXVyA_m-AAISyxcFy0ysn3Slidb8jsifOc4E3kZYFzzi-jBqC13UtSz2J7UPVRNsOaOxL84ukmKK_KL-HH0BRq0jd3HhruS3BNiPgxxhzcqkTpCAliXZlPpmEzhs4mgNYRVPz5IurNe78LZ1jFEuq-TYLTxG-WvBEEEGy0-I_yEYC9FPPDF9cnIgjrmwFPozQwepAB_UsdeTd5E7284A-boNmelEA4PoUOeSEphLN0Pu6_n5XBUt3bhsyRyLCaLjmr_bEDTB3jl6haQwXX9MdjLLoCgcA2s6I5VYl6OUPWuUPjCkj0v8B62dsKiGmLDH_nRDwwJZo0GXdvjnEXtm9c8S6n3H9gl9PuWYrOFaOV6BwRwzqqtLnIxbLok5_xI2rsRHa6dG5wBqyYVfvcPPnYdXYuux6zhFc-vuk6WKFTWVVNigrLbV1HhB16iv0T7HHs8VWhrQwMWBPTGhur37wzNWBHgouFs1i1hY3GmM-RUWe8ze-yw-aPZCV0lLc8GQxb0nOpgatEjqvM3h7ykQVBy1QwGV3oPEFsWsvBO7qLq0pVsfXGMtNcdYNyS9Fya29VlAPOTWv-e7KOzAr_Jzf9nwuYilvVrEpamO6ZM0VZGaY2vSYe44OU2wFDq2C8OQOViESiJK_iLB4RNaYJRGnOoo-UfiyHZCQZUG0lmQqSvscoa5kRNGndGZysinGZF6DWCXcvu"
    device_id:str = "5422118A-DE35-4554-A22F-F05D84D33288"
    token_id:str = "218521dd484fdaa7e26938b5b8acca2"

    response_context_id:str = "rc_56256756bf103a9b"
    request_context_id:str = "c_f8a53d26bb2909e0"
    request_id:str = "r_802f6dea5c21d9a9"



    return f'%5Bnull%2C%22%5B%5B%5C%22{text_encode}%5C%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C0%5D%2C%5B%5C%22ru%5C%22%5D%2C%5B%5C%22c_54cbf58b2b6820c0%5C%22%2C%5C%22r_f6705a0edd5fd98b%5C%22%2C%5C%22rc_8c9873803158bb84%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22AwAAAAAAAAAQANM7mBjXKZQ5bLHnwRk%5C%22%5D%2C%5C%22!RUalRh7NAAZeabWMfmlCS-pg_cCxre07ADQBEArZ1E7calwswLP7p8vVpj_dqlMs4Wl6eyFEMv6_-2Gm77k0p2ogmlDI9XT45nlj4tQvAgAAAPBSAAAACmgBB34AQfJCuljCK-EbPjXfLS8u4VzoIZvyjEbtDJaXB5Io1gQ6-hkLZHNXy3c173NQNEnYLMdjFf7yIpyLGMJ42g2KHBmrmQPEYTnYyFifbFXQplHIy8Cm_J-3-M8cuW1P9bm9-cikW4nylDbKIBr0s-CNUr-rk4L79oFiiz8T4jIEtNXbRgmv5myBj0LIwS3OsNI6RZ5iW08ylUMwY7hrPBP3n0u0dYnkx2ZLTc6NtUW3dBjIuipcOPSa5vm_7R-znZQrRw7O6loZL0Fxa5x6xh20FPGWaHZhAC1emNEy1kqDhS8i8AaX3FVc-pyzfBhELGr_w9mW5aPRjtnuGlPsxF9MXr5HsJiuw2Huhgx4klJhiRuAzCLOEWD-GViU4r2GxMwkAg7yH1Q0Q7hMC2OFX9A4M-4rsEH30cPrLYEC3jY_JhucFhaz4BvJzWNrOABNVCKHJbaL-YT3YIRJPfgzliTMAjfEuLrI9_EXirqqzQSoTM9HBMbuUnC8J5kJ8Q43tEdieX8wpkSyXK53lulGOG2_8jVjq5EgEatsOYLD0xMxr9wuZ-XnX23HBPK-6oGwc_-b6HuiA8xlWJoIdkKChE79RODbvFR-XPCsquO7Ogn1Cv8EyW6Z5R69nu0WliCfBa1C6li4_uW-VUF1BOiF2HZZZr65qWIBI5t5a47m4XjpdHqrlO0LhAFIJxeazytl8p1rlzNOFahnbg4tJa8deI9aX2FBpMpujEkGpYTa0fd_BBcrBRKE1CSxxt31ps51BCKhN9n-YymQWyovqyaQ6sMbWXV-E_c9oMyw3lzeqjWMzRUHpY66eL-TPl99fB_yE8kPoi3UnlK-T6qQC5Oh2aiA6zW3qj0MJK4Xw9csiuBsyxThgNeAjGK8tOEW-O1xIfsZwsiXvCHVdpM6rTr-JNX1fnkNI6OZVLUxLqaOeIb2i2jn0KSGYiGlN_w5Kd_61pE9Wj6lh3YlahItbobxf_0bQS4Ejv6qe6sPWuKri7kdZ99CbOGwa-DTEB4RS5dgIFBLzsbCWoMFIB0B2R1LV8ToFkWcpPdKaI-YSvY5eV3vEWw_tCGOIc9vqpEKPx2D-4Det3nOdg6VyU-TlRK-rVLXb9-7yyu4hjA_0GWw6SidWhS5yj9FoL2lzx4KUxU4-aPVLIUK9SxwYJu56cctiRm3FPLlAQ1NAd_i_hQn4tDcMYeslsXQJRgWkK2Uard2_9bqGqznNYmXJ1NVgHEOv95uoEbp_YRKR0cd7DmXQjcC0VxKCI-qdS87YAehSMs7lvrUj0lk_WnkTd7oxecrFH59ah7YU49xXg-Cl3gyjd6pJXR7wl5HeD4-fXLGsn_fdEYIc9v2LV3oNTkBDshjvMEdzv-UHQZ-CF_Prg%5C%22%2C%5C%22b71921d938fb7ae69ecdce553dcb0b83%5C%22%2Cnull%2C%5B1%5D%2C1%2Cnull%2Cnull%2C1%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B11%5D%5D%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2C%5B4%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%226403DEDA-F59D-4EC9-B543-AC941377BD3A%5C%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1770037908%2C926000000%5D%2Cnull%2C2%5D%22%5D&at=AEHmXlHrYgpkQzfnNLoNalQ4g610%3A1770018068736&'
    #return f'%5Bnull%2C%22%5B%5B%5C%22{text_encode}%5C%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C0%5D%2C%5B%5C%22ru%5C%22%5D%2C%5B%5C%22%5C%22%2C%5C%22%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22%5C%22%5D%2C%5C%22!n5ylnMTNAAZT9fabc_VCCBJk8GojLRM7ADQBEArZ1Iv9j8izQippc4GB-O5kYpkQyVhJsec4IUlm4a_7NyLliYXSLNe0GU0OMftoK6MzAgAAALpSAAAAJWgBB34AQQC3A_aXylaQQOK9bsR-3vMck6ZC-_0FVIpcSWgPnQd1B05gPK_PVkbLVt-GIKBKehRuQa_lLPJI4PbTkQf_40TAmQN_p4Q-liP21vkEdeJ4nwxlayEpha2a8xNSDuJVLxgA40nvqTQCrcaFIreLU_vNkqrb4Fo0f6Irub6r7SrQ2KgVJfMRDOj9-gH3GC9pNreYO7gu_DQj-TJSx3YQtsmplmKC-jiRFh2x5ZDvuejmm-jYoXTRYW7syQvs1t9w6Phs07fsBJw5_Djx1QT3AoyQVqhL6ARSbbYluyAgXeTEfKacIRfTEolklS7HmI1Ls9QT6Fxnt7om9RrW3lBlFzzwwxsnUhvh5Z2GJQ96rrCKP491gE0hLyQl-mxkMZfzumYWKM74PLOqPzxj63pyoACPX11JAAi_FTrBJmtVsq0kgf3SwiAvUPlY1Zm6e3v0EjJ0qbkuaT-zjN9bwyAbR6ZFix0QLPsVO7qwE03uJIVAujmzAZgCMFihHKv2auDVkxDLPtmGoXQk_55JTLaTgRrPTDzBhCyqZ_QjXsoSK5Ye3_yznVFZJbcaXSIilPHGjv3geUJnboOCcwk1q7FF2o3atD4lw5A3u1Il5OdTcCCUnK7WEbsJBmZvw-1z3t2Me5EtCvT-3ZHL9kllAzBspxheN4UPkbDms06qqB9vkGEv0qeMUOx6G8dTLJmya1og35kbOixtJ1MceHgSC2BI-EA4mg8nw-F9H6uvbsq2rFbS7OyA5GfPS09HUN8ukGeg9EzBtCscZzcDfMUZLuMPk7lUUiew-1lDYdnzvH7XmzA2PgI-icwYOWstUvqR-5LdG-tE7eKOncsgiSuicbvQDNC0BhIsmrVEZ5ZLl5LcERCHOtgNvfkRUsa8GpIdfaIoAc6fvJ2ycYRDXwXMBqK_T4JT_kDrj05huAjcwSrzLRkYv-3KT4VUPVlQ4_PtRcu0MIc6M3diMc1gUSkQb4CFYNgGAB3avxciIUq5kDMPhTIYQhmrwEPqC5vl5lUtNqrTwz-I9QzYZOrxGVq8OoTzm_VE8WVFpkKdbo30-nFUXLvaWoSFnOD6kyspCDLjbgtrSitNp-5LLHrcXhqP9oL1Oz0wZbKmETC86-MLOfYIbdcpHh5AQG4mQ4e1D70IhTi7owX4VPXqygcpSAO47o7cKyXgJKJNPaxCnff3522RZ8ggka1ZU5Bl4uJncEogVJJQdRBoTzS0dMGzp9alDZqqDwoc7LQUAYUTZetMPhKWxMnGiceUhVcIKCj8AgmCNnFQrR3TZQ%5C%22%2C%5C%22e6df889b0449cc80930990b0a3e72d0d%5C%22%2Cnull%2C%5B1%5D%2C1%2Cnull%2Cnull%2C1%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B0%5D%5D%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2C%5B4%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%220F739AC6-7E6A-4646-B0EF-145B23D1A238%5C%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1765624925%2C228000000%5D%5D%22%5D'



def decode_message(text: str) -> str:
    text_decode = urllib.parse.unquote(text)

    # return json.dumps(text_decode, indent=4, ensure_ascii=False)
    return text_decode.split()

def decode_message_a(encoded_str: str):
    # Повне розкодування назад у Python об'єкт
    unquoted = urllib.parse.unquote(encoded_str)
    try:
        data = json.loads(unquoted)
        # Оскільки всередині Google часто шле JSON у рядку, розпаковуємо вкладений шар
        if isinstance(data[1], str):
            data[1] = json.loads(data[1])
        return data
    except:
        return unquoted

test_text: str = "Hello< how 'are' u???"


test_text = "Hello< how 'are' u???"
encoded = encode_message(test_text)
print("[bold green]Encoded Result:[/bold green]\n", encoded)

decoded = decode_message(encoded)
print("\n[bold blue]Decoded Structure:[/bold blue]")
print(decoded)