import random

#using randint() to get a random number
first_number = 1
last_number = 20
guessed_number = random.randint(first_number, last_number)
#setting attempts and current_attempts
attempts = 5
current_attempts = 1

print(f"Я загадал число от {first_number} до {last_number}. У тебя {attempts} попыток!")

#using while
while attempts > 0:
    guess = int(input(f"Попытка {current_attempts}. Введите число: "))

    attempts = attempts - 1
    current_attempts = current_attempts + 1

    if guess == guessed_number:
        print("Ты угадал! Отличная работа.")
        break
    elif guess < guessed_number:
        print("Слишком мало! Осталось попыток:", attempts)
    elif guess > guessed_number:
        print("Слишком много! Осталось попыток:", attempts)