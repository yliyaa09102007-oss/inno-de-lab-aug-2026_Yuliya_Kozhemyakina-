#isactive is a variable that tells while whether to work or no
isactive = True
#starting Calculator
while isactive:
    first_number = input("Введите первое число: ")
    second_number = input("Введите второе число: ")

    #checking for valid values
    if first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)    #converting string to int
        second_number = int(second_number)

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
            result = first_number / second_number
            print(f"Результат: {first_number} / {second_number} = {result}")
        else:
            print("Что-то пошло не так. Скорее всего, вы ввели некорректный оператор!")
    else:
        print("Вы ввели некорректные значения!")

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




