# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_nums(num):
    sum = 0
    for i in str(num):
        if i != ",":
            sum += int(i)
    return sum

num = (input('Vvedite veshestvennoe chislo: '))
print(sum_nums(num))
