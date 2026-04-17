"""
Masala: Berilgan butun sonlar ro‘yxatidagi har bir sonni kvadratga ko‘taring (map orqali).
map() funksiyasi bilan ishlash
"""

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Asl ro'yxat: {sonlar}")

# Kvadratlar
kvadratlar = list(map(lambda x: x ** 2, sonlar))
print(f"Kvadratlar:  {kvadratlar}")

# Kub
kublar = list(map(lambda x: x ** 3, sonlar))
print(f"Kublar:      {kublar}")

# Celsius -> Fahrenheit
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = list(map(lambda c: round(c * 9/5 + 32, 1), celsius))
print(f"\nCelsius:    {celsius}")
print(f"Fahrenheit: {fahrenheit}")
