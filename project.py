import math

class Number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def modulus(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def display(self):
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {abs(self.imaginary)}i")

num = Number(3, 4)  
num.display()  
print(f"Модуль числа: {num.modulus()}") 
