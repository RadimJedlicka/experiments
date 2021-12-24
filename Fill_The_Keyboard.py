import os
os.system("cls")

keyboard = {1: 'qwertyuiop', 2: 'asdfghjkl', 3: 'zxcvbnm'}
klavesnice = {
    1: ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    2: ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    3: ['_', '_', '_', '_', '_', '_', '_']
}

print(' '.join(klavesnice[1]))
print('', ' '.join(klavesnice[2]))
print(' ', ' '.join(klavesnice[3]))

message = 'already in'
run = True
while run:
    entry = input('Type in some letter: ')
    os.system("cls")
    if '_' not in klavesnice[1] and '_' not in klavesnice[2] and '_' not in klavesnice[3]:
        run = False
    elif entry.upper().isalpha() is False or len(entry.upper()) > 1:
        print(' '.join(klavesnice[1]))
        print('', ' '.join(klavesnice[2]))
        print(' ', ' '.join(klavesnice[3]))
        print('wrong input!')

    elif entry.upper() in klavesnice[1] or entry.upper() in klavesnice[2] or entry.upper() in klavesnice[3]:
        print(' '.join(klavesnice[1]))
        print('', ' '.join(klavesnice[2]))
        print(' ', ' '.join(klavesnice[3]))
        print(message)
    elif entry in keyboard[1]:
        for index, symbol in enumerate(keyboard[1]):
            if symbol == entry:
                klavesnice[1][index] = entry.upper()
                print(' '.join(klavesnice[1]))
                print('', ' '.join(klavesnice[2]))
                print(' ', ' '.join(klavesnice[3]))
    elif entry in keyboard[2]:
        for index, symbol in enumerate(keyboard[2]):
            if symbol == entry:
                klavesnice[2][index] = entry.upper()
                print(' '.join(klavesnice[1]))
                print('', ' '.join(klavesnice[2]))
                print(' ', ' '.join(klavesnice[3]))
    elif entry in keyboard[3]:
        for index, symbol in enumerate(keyboard[3]):
            if symbol == entry:
                klavesnice[3][index] = entry.upper()
                print(' '.join(klavesnice[1]))
                print('', ' '.join(klavesnice[2]))
                print(' ', ' '.join(klavesnice[3]))
else:
    print(' '.join(klavesnice[1]))
    print('', ' '.join(klavesnice[2]))
    print(' ', ' '.join(klavesnice[3]))
    print('You have filled the whole keyboard :-)')
