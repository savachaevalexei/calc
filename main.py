
print(f"Пример ввода. Например, дано число 1+2i \n В программу необходимо передать в следующем виде: \n 1,2")
a, b = map(int, input("Введите действительную и мнимую часть 1-го числа через запятую: ").replace(" ", "").split(","))
c, d = map(int, input("Введите действительную и мнимую часть 2-го числа через запятую: ").replace(" ", "").split(","))
operator = input("Введите знак математической операции: +, * или / ").replace(" ", "")

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
     
    def __repr__(self):
        return "{}{:+}i".format(self.real, self.imag)
    
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)
     
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)
     
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)
 
z1 = ComplexNumber(a, b)
z2 = ComplexNumber(c, d)

if (operator == "+"):
    print("Сложение :", z1 + z2)
elif (operator == "*"):
    print("Умножение :",  z1 * z2)
elif (operator == "/"):
    print("Деление :",  z1 / z2)

