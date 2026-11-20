#Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.
def count_digits(num):
    """Считает количество цифр в целом числе."""
    num = abs(num)  # на случай, если число отрицательное
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


# Ввод с обработкой исключений в начале
try:
    n = int(input("Введите целое число: "))
    result = count_digits(n)
    print("Количество цифр в числе:", result)

except ValueError:
    print("Неправильно ввели! Нужно ввести целое число.")