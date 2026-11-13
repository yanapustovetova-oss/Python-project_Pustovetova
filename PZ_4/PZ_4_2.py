
# Дано целое число N (> 0). Найти сумму 1^2 + 2^2 + ... + N^2.

# Ввод N с обработкой исключений
n = input("Введите целое число N (> 0): ")
while type(n) != int:
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели! N должно быть целым и > 0.")
        n = input("Введите целое число N (> 0): ")

#  Вычисление суммы
total = 0
for k in range(1, n + 1):
    total += k ** 2

print(f"Сумма 1^2 + 2^2 + ... + {n}^2 = {total}")