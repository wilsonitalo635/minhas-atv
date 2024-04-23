class Triangulo:
    def __init__(self, lado_1, lado_2, lado_3):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
        
    def calcular_perimetro(self):
        return self.lado_1 + self.lado_2 + self.lado_3
    
    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado_1) * (s - self.lado_2) * (s - self.lado_3)) ** 0.5
        return area

triangulo = Triangulo(3, 4, 5)
print("Perímetro do triângulo:", triangulo.calcular_perimetro())
print("Área do triângulo:", triangulo.calcular_area())