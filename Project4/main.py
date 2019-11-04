import requests
import my_functions

language = my_functions.lang_inp()
if language == 1:
    import local_en as loc
elif language == 2:
    import local_ru as loc


def translate(s, language):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'trnsl.1.1.20191104T045720Z.2fd097c84b992f6b.29323d8f477c6e7ffae9550a7c8064a0f77da6a7'
    lang = language
    params = {
        'key': KEY,
        'text': s,
        'lang': lang,
    }
    response = requests.get(URL, params=params).json()
    if response['code'] == 200:
        return response['text'][0]
    else:
        return loc.ERROR


print(loc.INPUT_END)
l = input(loc.INPUT_LANG)
while True:
    if l == '1' or l == '1.' or l == 'en-ru' or l == '1. en-ru':
        lang_trans = 'en-ru'
        break
    elif l == '2' or l == '2.' or l == 'ru-en' or l == '2. ru-en':
        lang_trans = 'ru-en'
        break
    else:
        l = input(loc.CHECK_LANG)
s = input(loc.INPUT_TEXT)
while s != '0':
    print(translate(s, lang_trans))
    s = input(loc.INPUT_TEXT)

