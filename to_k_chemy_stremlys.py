class NumberAnalyzer:
    def __init__(self, number: int):
        # Инициализируем объект и сохраняем число внутри него
        self.number = number

    def check_sign(self):
        if self.number > 0:
            print("Положительное: да")
        elif self.number < 0:
            print("Положительное: нет")
        else:
            print("0 является ни положительным, ни отрицательным числом!")

    def check_even_odd(self):
        if self.number % 2 == 0:
            print("Чётное: да")
        else:
            print("Чётное: нет")

    def check_division(self, divider: int):
        # Универсальный метод для проверки деления на любое число
        if self.number % divider == 0:
            print(f"Делится на {divider}: да")
        else:
            print(f"Делится на {divider}: нет")

    def _is_prime(self) -> bool:
        # Нижнее подчеркивание говорит о том, что это внутренний метод класса
        if self.number <= 1:
            return False
        if self.number == 2:
            return True
        if self.number % 2 == 0:
            return False
        for i in range(3, int(self.number**0.5) + 1, 2):
            if self.number % i == 0:
                return False
        return True

    def check_prime(self):
        if self._is_prime():
            print("Простое число: да")
        else:
            print("Простое число: нет")

    def count_digits(self):
        count = len(str(abs(self.number)))
        print(f"Количество цифр: {count}")

    def run_all_checks(self):
        # Метод-оркестратор, который запускает все проверки разом
        print(f"\nВаше число: {self.number}")
        self.check_sign()
        self.check_even_odd()
        self.check_division(3)
        self.check_division(5)
        self.check_prime()
        self.count_digits()


# --- Основная часть программы ---

while True:
    user_input = input("Введи свое число для проверки: ").strip()
    try:
        num = int(user_input)
        break
    except ValueError:
        print("Введи целое число для проверки!")

# Создаем экземпляр нашего класса (объект) и передаем ему число
analyzer = NumberAnalyzer(num)

# Запускаем все проверки одной строчкой
analyzer.run_all_checks()
