#  Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
a = float(input("Введите число: "))
if a % 2 == 0:
    result = a // 4
    print(result)
else:
    result1 = a * 5
    print(result1)