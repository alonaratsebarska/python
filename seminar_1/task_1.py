# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = (int(input('Vvedite cyfru, oboznachajushchuju den nedeli: ')))

def DaysOfWeek(number):
    if number == 6 or number == 7:
        result = 'Da. Segodnia vychodnoj den. Pozdravliaju!!!'
    elif number >= 1 and number <= 5:
        result = 'Net. Segodnia rabochij den. Idi na rabotu / uchebu :) '
    else:
        result = 'Vvedite chislo v diapazone ot 1-go do 7-mi'
    return result

print(DaysOfWeek(num))           
