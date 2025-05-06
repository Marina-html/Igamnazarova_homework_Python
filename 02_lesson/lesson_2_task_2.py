def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"

div = int(input("Введите год:"))
result = is_year_leap(div)
print(f"Год {div}: {result}")