# Дополнительная задачи из занятия 2(которые не успели решить)
# СТРОКИ
# A. Вводится n строк. Вывести количество пробелов
strings = input()
print(strings.count(" "))

# Б. Пример - Я пришел учиться.
#Вводится n строк, каждая строка – одно слово. Составить из них
#предложение с пробелами и точкой в конце.

strings_1 = input()
strings_2 = input()
strings_3 = input()
print(f'{strings_1} {strings_2} {strings_3}.')


# ФУНКЦИИ
# A.
operation_input = input('Выберите операцию: +-/*\n')
def my_func(x, y):
    if operation_input == '+':
        return f'{x} + {y} = {x + y}'
    elif operation_input == '-':
        return f'{x} - {y} = {x - y}'
    elif operation_input == '*':
        return f'{x} * {y} = {x * y}'
    elif operation_input == '/':
        return f'{x} / {y} = {x / y}'

print(my_func(9, 3))

# Б.
def my_func(n, m):
    summ = (n * m) / 10
    result = n + summ
    return result

print(my_func(22500, 5))