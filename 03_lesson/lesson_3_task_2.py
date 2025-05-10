from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy", "89162222222"),
    Smartphone("IPhone", "17", "89162222223"),
    Smartphone("Motorola", "One", "89162222224"),
    Smartphone("Sony", "Plus", "89162222225"),
    Smartphone("Xiaomi", "New", "89162222226"),
]

for smartphone in catalog:
    print(f"{smartphone.brand_phone} {smartphone.model_phone} {smartphone.number_phone}")
