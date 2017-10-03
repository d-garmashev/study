import requests
import io

key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

def detect_lang(text, api_key=key):

    url_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'

    params = {
        'key': api_key,
        'text': text
        }

    response = requests.get(url_detect, params=params).json()

    return response['lang']

def translate_it(source_file_path, result_file_path, to_lang='ru', api_key=key):

    url_translate = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    with io.open(source_file_path, 'r', encoding='utf8') as f:
         text = f.read()

    from_lang = detect_lang(text)

    params = {
        'key': api_key,
        'lang': '-'.join([from_lang, to_lang]),
        'text': text
        }

    response = requests.get(url_translate, params=params).json()
    text_result = ' '.join(response.get('text', []))

    with io.open(result_file_path, 'w', encoding='utf8') as f:
        f.write(text_result)

# DE -> RU translation
translate_it('DE.txt', 'DE_RU.txt')

# ES -> RU translation
translate_it('ES.txt', 'ES_RU.txt')

# FR -> RU translation
translate_it('FR.txt', 'FR_RU.txt')

# FR -> EN translation
translate_it('FR.txt', 'FR_EN.txt', 'en')

