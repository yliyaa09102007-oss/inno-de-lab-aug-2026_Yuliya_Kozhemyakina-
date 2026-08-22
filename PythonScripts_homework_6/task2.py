length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
area = length * width
print(f"Площадь прямоугольника: {area}")

#another variant, where we check for correct input (user can enter smth like "sdsdsd")

length = input("Введите длину прямоугольника: ")
width = input("Введите ширину прямоугольника: ")

#isdigit is method to check if string consists of numbers only
if length.isdigit() and width.isdigit():
    area = int(length) * int(width)
    print(f"Площадь прямоугольника: {area}")
else:
    print("Вы ввели некорректное значение!")