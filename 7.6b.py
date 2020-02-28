# Задача. Вивести дані про книги, в яких кількість сторінок більше 150. Поля
# структури: Автор, Кількість сторінок, Тираж, Рік видання.
# Мельничук Олена Костянтинівна 122В

while True:
    while True:
        try:
            x = int(input('Enter number of pages 1 book: '))
            y = int(input('Enter number of pages 2 book: '))
            z = int(input('Enter number of pages 3 book: '))
            break
        except ValueError :
            print('Please enter a number: ')
    keys=['author','circulation','edition','pages']
    a = [input('Enter author 1 book: '), int(input('Enter circulation 1 book: ')), int(input('Enter edition 1 book: ')), x]
    b = [input('Enter author 2 book: '), int(input('Enter circulation 2 book: ')), int(input('Enter edition 2 book: ')), y]
    c = [input('Enter author 3 book: '), int(input('Enter circulation 3 book: ')), int(input('Enter edition 3 book: ')), z]
    info1 = {keys: a for(keys, a) in zip(keys, a) if x > 150}
    info2 = {keys: b for(keys, b) in zip(keys, b) if y > 150}
    info3 = {keys: c for(keys, c) in zip(keys, c) if z > 150}
    print(info1,info2,info3)
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break
