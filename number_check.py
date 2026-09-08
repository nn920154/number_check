
while True:
    number_user = input("Введи свое число для проверки: ").strip()
    try:
        number = int(number_user)
        break
    except ValueError:
        print("Введи целое число для проверки!")


print(f"\nВаше число: {number}")


def what_number(number):
    if number > 0:
        print("Положительное: да")
    elif number < 0:
        print("Положительное: нет")
    else:
        print("0 является не положительным и не отрицательным числом!")


def even_or_odd(number):
    if number % 2 == 0:
        print("Чётное: да")
    else:
        print("Чётное: нет")


def division_by_3(number):
    if number % 3 == 0:
        print("Делится на 3: да")
    else:
        print("Делится на 3: нет")


def division_by_5(number):
    if number % 5 == 0:
        print("Делится на 5: да")
    else:
        print("Делится на 5: нет")


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def prost(number):
    if is_prime(number):
        print("Простое число: да")
    else:
        print("Простое число: нет")


what_number(number)
even_or_odd(number)
division_by_3(number)
division_by_5(number)
prost(number)
print(f"Количество цифр: {len(str(abs(number)))}")
