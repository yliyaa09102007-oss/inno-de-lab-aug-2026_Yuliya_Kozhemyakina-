temperature_celsius = input("Введите температуру в градусах Цельсия: ")
#using the same method to check if the value is valid
if temperature_celsius.isdigit():
    temperature_fahrenheit = int(temperature_celsius) * 9 / 5 + 32
    print(f"{temperature_celsius}°C это {temperature_fahrenheit}°F")
else:
    print("Вы ввели некорректное значение!")