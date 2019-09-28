from cities import a
import random




print('Давайте сыграем в "города".\nПравла:\nКаждый называемый город должен начинаться с буквы, на которую оканчивается предыдущий.\nЕсли название пердыдущего города оканчивается на "ъ", "ь" или "ы", то можно называть город начинающейся с предпоследней буквы предыдущего.\nЗаглавная "Ё" заменена на "Е"\n\nЯ начинаю:')

#Генерация первого случайного города
key = chr(ord('А') + random.randint(0, 32))
while key == 'Ё' or key == 'Ь' or key == 'Ы' or key == 'Ъ':
    key = chr(ord('А') + random.randint(0, 32))

n = len(a[key])
j = random.randint(0, n -1)
inp = ''

while n != 0 and inp != 'Сдаться':
    #Ввод
    print(a[key][j])
    a[key][j] = '1' + a[key][j]
    inp = input()

#Проверки корректности введенного слова
    #Проверка наличия ключа в словаре
    while ord(key) > (ord('А') + 32) or ord(key) < (ord('А')) or key == 'Ё' or key == 'Ь' or key == 'Ы' or key == 'Ъ':
        inp = input('Я не знаю такого города. Назовите другой: ')
    #Проверка слова на повторение
    key = inp[0].upper()
    while ('1' + inp) in a[key]:
        inp = input('Такой город уже был. Назовите другой: ')
    #Проверка наличия слова в списке по ключу
    while inp not in a[key]:
        inp = input('Я не знаю такого города. Назовите другой: ')
    m = len(a[key])
    for x in range(m):
        if a[key][x] == inp:
            a[key][x] = '1' + inp
            break
    print(a[key])



# Проверки корректности выводимого слова
    i = len(inp) - 1
    key = inp[i].upper()
    #Проверка наличия ключа в словаре и смена буквы в противном случае
    while key == 'Ё' or key == 'Ь' or key == 'Ы' or key == 'Ъ':
        i -= 1
        key = inp[i].upper()

    n = len(a[key])
    #Генерация нового слова
    j = random.randint(0, n - 1)
    cond = False
    #Проверка слова на повторение и его замена в случае повторения
    if a[key][j][0] == '1':
        cond = True
        for x in range(n):
            if a[key][x][0] != '1':
                cond = False
                j = x
                break

    if cond:
        print('Я больше не знаю городов на эту букву(\nВы выиграли!')
        break




#Конец игры
if n == 0:
    print('Я больше не знаю городов на эту букву(\nВы выиграли!')
if inp == 'Сдаться':
    print('Вы проиграли!')
print('Игра окончена')
