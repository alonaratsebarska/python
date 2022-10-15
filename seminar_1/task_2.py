# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 1 Variant
def check_predicate_and_show_result(x, y, z):
    left = not(x or y or z )
    right = not x and not y and not z
    result = left == right
    if result == True:
        print('Utverzhdenije istinno (True)')
    else:
        print('Utverzhdenije lozhno (False)')

x = int(input("Vvedite znachenije koordinaty Ox: "))
y= int(input("Vvedite znachenije koordinaty Oy: "))
z = int(input("Vvedite znachenije koordinaty Oz: "))
check_predicate_and_show_result(x,y,z)

# 2 Variant
# x = int(input("Vvedite znachenije koordinaty Ox: "))3
# y= int(input("Vvedite znachenije koordinaty Oy: "))
# z = int(input("Vvedite znachenije koordinaty Oz: "))

# left = not(x or y or z )
# right = not x and not y and not z
# print(left == right)