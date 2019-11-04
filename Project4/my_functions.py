def lang_inp():
    language = input('Choose language:\n1. English\n2. Russian\n')
    while True:
        if (language.lower() == 'english' or language.lower() == 'en' or language == '1' or language == '1.' or
                language.lower() == '1. english'):
            language = 1
            break
        elif (language.lower() == 'russian' or language.lower() == 'ru' or language == '2' or language == '2.' or
                language.lower() == '2. russian'):
            language = 2
            break
        else:
            language = input('Choose language from the proposed:\n1. English\n2. Russian\n')
    return language
