from my_functions import lang_inp
from translator import translate

language = lang_inp()
if language == 1:
    import local_en as loc
elif language == 2:
    import local_ru as loc


print(loc.INPUT_END)
lang = input(loc.INPUT_LANG)
while True:
    if lang == '1' or lang == '1.' or lang == 'en-ru' or lang == '1. en-ru':
        lang_trans = 'en-ru'
        break
    elif lang == '2' or lang == '2.' or lang == 'ru-en' or lang == '2. ru-en':
        lang_trans = 'ru-en'
        break
    else:
        lang = input(loc.CHECK_LANG)
s = input(loc.INPUT_TEXT)
while s != '0':
    print(translate(s, lang_trans))
    s = input(loc.INPUT_TEXT)
