import random

#using randint() to get a random number from 1 to 20
guessed_number = random.randint(1,20)
#setting attempts and current_attempts
attempts=5
current_attempts=1

print("Я загадал число от 1 до 20. У тебя 5 попыток!")

#using while
while attempts > 0:
    print(f"Попытка {current_attempts}. Введите число:")
    guess=int(input())

    attempts=attempts-1
    current_attempts=current_attempts+1

    if guess==guessed_number:
        print("Ты угадал! Отличная работа.")
        break
    elif guess<guessed_number:
        print("Слишком мало! Осталось попыток:", attempts)
    elif guess>guessed_number:
        print("Слишком много! Осталось попыток:", attempts)