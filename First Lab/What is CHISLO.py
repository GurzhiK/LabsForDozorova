import random

def guess_the_number(start, end, attempts):
    secret_number = random.randint(start, end)
    for i in range(attempts):
        guess = int(input("Введите число: "))
        if guess == secret_number:
            print(f"Вы победили! Загаданное число было: {secret_number}.")
            return
        elif guess < secret_number:
            print("Больше")
        else:
            print("Меньше")
    print("Потрачено")

def start_game():
    start = int(input("Введите нижнюю границу диапозона чисел: "))
    end = int(input("Введите верхнюю границу диапозона чисел: "))
    attempts = int(input("Введите число попыток: "))
    guess_the_number(start, end, attempts)
    play_again = input("Хотите сыграть еще: (да/нет) ")
    if play_again.lower() == "да":
        start_game()

start_game()