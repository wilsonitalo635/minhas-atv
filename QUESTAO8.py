class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)

retangulo1 = Retangulo(5, 10)
print("Área do retângulo:", retangulo1.calcular_area())
print("Perímetro do retângulo:", retangulo1.calcular_perimetro())