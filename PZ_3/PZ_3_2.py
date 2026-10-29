#Данны два числа. Вывести вначале большее, а затем меньшее из них.
while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка! Введите числа. ")

#Сравнение и вывод
if num1 > num2:
    print(f"Большее число: {num1}")
    print(f"Меньшее число: {num2}")
else:
    print(f"Большее число: {num2}")
    print(f"Меньшее число: {num1}")





