language = input('Choose language:\nEnglish (or en)\nRussian (or ru)\n')
while True:
    if language.lower() == 'english' or language.lower() == 'en':
        import loc_en as loc
        break
    elif language.lower() == 'russian' or language.lower() == 'ru':
        import loc_ru as loc
        break
    else: language = input('Choose language from the proposed:\nEnglish\nRussian\n')

def fib(n):
    fib_lasts = [1, 1]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        for i in range(n - 2):
            fib_lasts[0], fib_lasts[1] = fib_lasts[1], fib_lasts[0] + fib_lasts[1]
        return fib_lasts[1]

def sys_2(n):
    n_2 = ''
    while n != 0:
        n_2 = str(n % 2) + n_2
        n = n // 2
    return n_2


def sys_3(n):
    n_3 = ''
    while n != 0:
        n_3 = str(n % 3) + n_3
        n = n // 3
    return n_3


def sys_4(n):
    n_4 = ''
    while n != 0:
        n_4 = str(n % 4) + n_4
        n = n // 4
    return n_4

def sys_8(n):
    n_8 = ''
    while n != 0:
        n_8 = str(n % 8) + n_8
        n = n // 8
    return n_8


def sys_16(n):
    n_16 = ''
    while n != 0:
        c = n % 16
        if 0 <= c <= 9: n_16 = str(c) + n_16
        elif c == 10: n_16 = 'A' + n_16
        elif c == 11: n_16 = 'B' + n_16
        elif c == 12: n_16 = 'C' + n_16
        elif c == 13: n_16 = 'D' + n_16
        elif c == 14: n_16 = 'E' + n_16
        elif c == 15: n_16 = 'F' + n_16
        n = n // 16
    return n_16


def main():
    x = int(input(loc.TXT_INPUT_X))
    print(loc.TXT_INPUT_INP1_1)
    print(loc.TXT_INPUT_INP1_2)
    print(loc.TXT_INPUT_INP1_3)
    inp1 = input()
    while True:
        try:
            inp1 = int(inp1)
        except ValueError:
            inp1 = input(loc.TXT_CHECK_1)
        else:
            break

    while True:
        if inp1 != 1 and inp1 != 2:
            inp1 = input(loc.TXT_CHECK_2)
            while True:
                try:
                    inp1 = int(inp1)
                except ValueError:
                    inp1 = input(loc.TXT_CHECK_1)
                else:
                    break
        else: break

    if inp1 == 1:
        print( fib(x) )
    elif inp1 == 2:
        print(loc.TXT_CHOOSE_OF_SYSTEM)
        print(2)
        print(3)
        print(4)
        print(8)
        print(16)

        inp2 = input()
        while True:
            try:
                inp2 = int(inp2)
            except ValueError:
                inp2 = input(loc.TXT_CHECK_1)
            else:
                break

        while True:
            if inp2 != 2 and inp2 != 3 and inp2 != 4 and inp2 != 8 and inp2 != 16:
                inp2 = input(loc.TXT_CHECK_2)
                while True:
                    try:
                        inp2 = int(inp2)
                    except ValueError:
                        inp2 = input(loc.TXT_CHECK_1)
                    else:
                        break
            else: break

        if inp2 == 2:
            print( sys_2(x) )
        elif inp2 == 3:
            print( sys_3(x) )
        elif inp2 == 4:
            print( sys_4(x) )
        elif inp2 == 8:
            print( sys_8(x) )
        elif inp2 == 16:
            print( sys_16(x) )


main()