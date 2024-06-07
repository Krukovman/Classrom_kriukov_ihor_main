
import random


def main():
    print("Добро пожаловать в викторину случайных чисел!")
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    if start >= end:
        print("Начало диапазона должно быть меньше конца диапазона!")
        return

    number = random.randint(start, end)
    attempts = 3  # Устанавливаем количество попыток

    while attempts > 0:
        print(f"Осталось попыток: {attempts}")
        guess = int(input(f"Угадайте число между {start} и {end}: "))
        if guess < number:
            print(f"слишком маленькое число. у тебя еще {attempts - 1} попытки!")
        elif guess > number:
            print(f"Число слишком большое. у тебя еще {attempts - 1} попытки!")
        else:
            print(f"Поздравляю! Вы угадали число {number}!")
            break
        attempts -= 1

    if attempts == 0:
        print(f"Ваши попытки исчерпаны , загаданное число: {number}.")
        print("спасибо за игру")


if __name__ == "__main__":
    main()
# конец кода
