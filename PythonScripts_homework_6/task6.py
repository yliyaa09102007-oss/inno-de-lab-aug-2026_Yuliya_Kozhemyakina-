#isactive is a variable that tells while whether to work or no
isactive = True
#starting Calculator
while isactive:
    #now using try/except to check for valid input
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите число!")
        continue

    operation_sign = input("Выберите оператор: (+, -, *, /): ")
    if operation_sign == "+":
        result = first_number + second_number
        print(f"Результат: {first_number} + {second_number} = {result}")
    elif operation_sign == "-":
        result = first_number - second_number
        print(f"Результат: {first_number} - {second_number} = {result}")
    elif operation_sign == "*":
        result = first_number * second_number
        print(f"Результат: {first_number} * {second_number} = {result}")
    elif operation_sign == "/":
        if second_number != 0:
            result = first_number / second_number
            print(f"Результат: {first_number} / {second_number} = {result}")
        else:
            print("Деление на ноль!")
    else:
        print("Что-то пошло не так. Скорее всего, вы ввели некорректный оператор!")


    print("") #just an empty line
    isactive2 = True
    while isactive2:
        answer = input("Желаете продолжить? Да/Нет: ")
        if answer == "Да":
            isactive = True
            isactive2 = False
        elif answer == "Нет":
            print("Завершение работы...")
            isactive = False
            isactive2 = False
        else:
            print("Некорректный ввод. Попробуйте снова...")
    print("")




