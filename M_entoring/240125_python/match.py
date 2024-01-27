# match case
# 다른 언어들에서 switch case


number = input('숫자입력')

number = int(number)

match number:
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print('잘못 ')


if number == 1:
    print(1)
elif number == 2:
    print(2)
else:
    print('잘못 ')

