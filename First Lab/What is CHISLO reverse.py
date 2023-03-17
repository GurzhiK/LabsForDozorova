print("Загадай любое целое число от 1 до 100")

low = 1
high = 100

while True:
    guess = (low + high) // 2
    response = input(f"Загаданное число: {guess}? (да/больше/меньше/нет): ")

    if response == "да":
        print("Отлично! Я отгадала!")
        break
    elif response == "меньше":
        high = guess
    elif response == "больше":
        low = guess + 1
    elif response == "нет":
        print("Потрачено.")
    else:
        print("Вы можете вводить только эти слова: да,больше,меньше,нет")