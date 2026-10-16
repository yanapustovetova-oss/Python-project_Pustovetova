# Запрашиваем у пользователя трёхзначное число
try:
    number = int(input("Введите трёхзначное число: "))

    if  100 <= number <= 999:


        hundreds = number // 100           # сотни
        tens = (number // 10) % 10         # десятки
        units = number % 10                # единицы

        # Меняем местами сотни и десятки
        new_number = tens * 100 + hundreds * 10 + units
        print("Новое число:", new_number)
    else:
        print("Ошибка! число должно быть трехзначным")

except ValueError:
    print("Ошибка! Нужно ввести целое число.")

