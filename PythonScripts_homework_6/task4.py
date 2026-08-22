number = input("Введите целое число: ")

if number.isdigit():
    if(int(number)%2==0):
        print(f"Число {number} - чётное.")
    else:
        print(f"Число {number} - нечётное.")
else:
    print("Вы ввели некорректное значение!")