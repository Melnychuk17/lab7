# Дано символи s1, s2, .... Відомо, що символ s1 відмінний від пробілу і що серед s2,
# s3, ... є хоча б один пробіл. Розглядаються s1, ..., sn - символи, що передують першому
# пробілу (n заздалегідь не відомо). Перетворити послідовність s1, ..., sn, видаливши з неї
# всі символи, які не є буквами.
# Мельничук Олена Костянтинівна 122В

while True:
    a=input('Enter symbols: ')
    s=set()
    if a[0]!=' ':
        for i in a:
            if i==' ':
                break
            if i.isalpha() :
                s.add(i)
        print(s)
    else:
        print('Space not 1')
    result = input('Want to restart? If yes - 1, no - other:  ')
    if result == '1':
        continue
    else:
        break

