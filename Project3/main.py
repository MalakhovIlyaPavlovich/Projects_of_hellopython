language = input('Choose language:\n1. English\n2. Russian\n')
while True:
    if (language.lower() == 'english' or language.lower() == 'en' or language == '1' or language == '1.' or
        language.lower() == '1. english'):
        import local_en as loc
        break
    elif (language.lower() == 'russian' or language.lower() == 'ru' or language == '2' or language == '2.' or
          language.lower() == '2. russian'):
        import local_ru as loc
        break
    else: language = input('Choose language from the proposed:\n1. English\n2. Russian\n')

print(loc.RULES_1, chr(11044), loc.RULES_2, chr(127873), loc.RULES_3, chr(11035),
      loc.RULES_4, sep=''
)
# MAZE INITIALIZATION
nx = 21
ny = 11
a = [ [0 for i in range(nx)] for i in range(ny)]
# Creating borders
for i in range(ny):
    for j in range(nx):
        if i == 0 or i == ny - 1 or j == 0 or j == nx - 1:
            a[i][j] = 11035
        else:
            a[i][j] = 11036

# Creating walls
for i in range(5):
    a[3][12 + i] = 11035
    a[3 + i][12] = 11035
    a[7][12 + i] = 11035
    if i != 2:  a[3 + i][16] = 11035
for i in range(5):
    a[2][2 + i] = 11035
    a[8][2 + i] = 11035
for i in range(7):
    a[2 + i][2] = 11035
for i in range(5):
    a[4 + i][6] = 11035
for i in range(2):
    a[4][4 + i] = 11035
for i in range(2):
    a[5 + i][4] = 11035

# Target (gift)
a[5][5] = 127873


# FIRST PRINT MAZE
x = 14
y = 5
a[y][x] = 11044
for i in range(ny):
    for j in range(nx):
        print(chr(a[i][j]), sep='', end ='')
    print()

# MAZE MOVEMENT
while y != 5 or x != 5:
    inp = input()
    if (inp.lower() == 'w' or inp.lower() == 'ц') and a[y - 1][x] != 11035:
        a[y][x] = 11036
        y -= 1
        a[y][x] = 11044
    elif (inp.lower() == 'a' or inp.lower() == 'ф') and a[y][x - 1] != 11035:
        a[y][x] = 11036
        x -= 1
        a[y][x] = 11044
    elif (inp.lower() == 's' or inp.lower() == 'ы') and a[y + 1][x] != 11035:
        a[y][x] = 11036
        y += 1
        a[y][x] = 11044
    elif (inp.lower() == 'd' or inp.lower() == 'в') and a[y][x + 1] != 11035:
        a[y][x] = 11036
        x += 1
        a[y][x] = 11044

    # Print maze
    for i in range(ny):
        for j in range(nx):
            print(chr(a[i][j]), sep='', end='')
        print()

print(loc.END)