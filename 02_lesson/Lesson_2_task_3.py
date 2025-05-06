import math

def square(back):
    return math.ceil(back * back)
back = float(input("Сторона квадрата: "))

print(f"Площадь квадрата: {math.ceil(back * back)}")

