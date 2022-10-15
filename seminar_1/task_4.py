# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# 1 Variant
def whats_range_of_points(num):
    res = ''
    if num == 1 or num == 4:
        res = 'Diapazon vozmozhnych koordinatnych tochek v ykazannoj chetverti : ot 0, 1, 2, 3, ...... ∞'
    elif num == 2 or num == 3:
        res = 'Diapazon vozmozhnych koordinatnych tochek v ykazannoj chetverti : ot 0, -1, -2, -3, ...... ∞'
    return res    

quadrant_number = int(input("Vvedite nomer chetverti koordinatnoj ploskosti (ot 1 do 4): "))
if quadrant_number < 0 or quadrant_number > 4:
    print('Vvodite chisla tolko v diapazone ot 1 do 4 vkluchitelno')
    print(whats_range_of_points(quadrant_number))
else:
    print(whats_range_of_points(quadrant_number))    

# 2 Variant (Bolee podrobnyj)
# def whats_range_of_points(num):
#     res = ''
#     if num == 1:
#         res = 'Diapazon tochek v ykazannoj chetverti :\nKoordinata X: ot 0, 1, 2, 3, ...... ∞\nKoordinata Y: ot 0, 1, 2, 3, ...... ∞'
#     elif num == 2:
#         res = 'Diapazon tochek v ykazannoj chetverti :\nKoordinata X: ot 0, -1, -2, -3, ...... ∞\nKoordinata Y: ot 0, 1, 2, 3, ...... ∞'
#     elif num == 3:
#         res = 'Diapazon tochek v ykazannoj chetverti :\nKoordinata X: ot 0, -1, -2, -3, ...... ∞\nKoordinata Y: ot 0, -1, -2, -3, ...... ∞' 
#     else:
#         res = 'Diapazon tochek v ykazannoj chetverti :\nKoordinata X: ot 0, 1, 2, 3, ...... ∞\nKoordinata Y: ot 0, -1, -2, -3, ...... ∞'   
#     return res   

# quadrant_number = int(input("Vvedite nomer chetverti koordinatnoj ploskosti (ot 1 do 4): "))
# if quadrant_number < 0 or quadrant_number > 4:
#     print('Vvodite chisla tolko v diapazone ot 1 do 4 vkluchitelno')
#     print(whats_range_of_points(quadrant_number))
# else:
#     print(whats_range_of_points(quadrant_number)) 
