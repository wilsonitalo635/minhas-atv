class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)
        
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return f"{self.nome} foi aprovado!"
        else:
            return f"{self.nome} foi reprovado."

notas_wilson = [7.5, 8.0, 6.5, 9.0]
wilson = Estudante("Wilson", 17, notas_wilson)
print('Média de', wilson.nome, ":", wilson.calcular_media())
print(wilson.verificar_aprovacao())

notas_pedro = [5.0, 5.5, 4.0, 6.0]
pedro = Estudante("Pedro", 17, notas_pedro)
print('Média de', pedro.nome, ":", pedro.calcular_media())
print(pedro.verificar_aprovacao())