# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check_quadrant(x, y):
    result = ''
    if x > 0 and y > 0:
        result = 'Quadrant 1'
    elif x < 0 and y < 0:
        result = 'Quadrant 3'
    elif (x > 0 or y > 0) and (x < 0 or y < 0):
        if x < 0 and y > 0:
            result = 'Quadrant 2'
        elif y < 0 and x > 0:
            result = 'Quadrant 4'
    return result        
                
x = int(input("Vvedite znachenije koordinaty Ox: "))
y= int(input("Vvedite znachenije koordinaty Oy: "))
if x == 0 or y == 0:
    print('Vvodite polozhtelnyje ili zhe otricatelnyje znachenija tochek koordinat, ne ravniajuschiesia nulu!')
    print(check_quadrant(x,y))
else:
    print(check_quadrant(x,y))
