import requests

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
        return 'ERROR ' + str(response['code'])