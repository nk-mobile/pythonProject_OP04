import math
# Сторона квадрата
a = float(input("Введите длину стороны квадрата : "))

def square(x):
    # Периметр квадрата
    perimetr = 4 * x
    # Площадь
    area = x ** 2
    # Диагональ
    diagonal = x *math.sqrt(2)
    return (perimetr, area, diagonal)

result = square(a)
print(f"Периметр, Площадь, Диагональ : {result}")