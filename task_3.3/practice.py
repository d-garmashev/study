import requests
import io

def translate_it(source_file_path, result_file_path, from_lang, to_lang='ru'):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    with io.open(source_file_path, 'r', encoding='utf8') as f:
         text = f.read()

    params = {
        'key': key,
        'lang': '-'.join([from_lang, to_lang]),
        'text': text
        }

    response = requests.get(url, params=params).json()
    text_result = ' '.join(response.get('text', []))

    with io.open(result_file_path, 'w', encoding='utf8') as f:
        f.write(text_result)

# DE -> RU translation
translate_it('DE.txt', 'DE_RU.txt', 'de')

# ES -> RU translation
translate_it('ES.txt', 'ES_RU.txt', 'es')

# FR -> RU translation
translate_it('FR.txt', 'FR_RU.txt', 'fr')

# FR -> EN translation
translate_it('FR.txt', 'FR_EN.txt', 'fr', 'en')

