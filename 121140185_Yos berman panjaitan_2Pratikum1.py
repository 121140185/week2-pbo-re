import math

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def log(self):
        return Calculator(math.log(self.value))

    def __str__(self):
        return f"Hasil: {self.value}"

# Contoh penggunaan
a = Calculator(10)
b = Calculator(2)

print(a + b)       # Penjumlahan
print(a - b)       # Pengurangan
print(a * b)       # Perkalian
print(a / b)       # Pembagian
print(a ** b)      # Pangkat
print(b.log())     # Logaritma
