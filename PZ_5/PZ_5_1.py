#напечатать сорок любых символов
def print_forty_chars(char):
    'печатает 40 заданных символов'
    print(char * 40)
s = input("Введите символ: ")
print_forty_chars(s)