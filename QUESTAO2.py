class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        
    def emitir_som(self):
        pass
    
    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Espécie: {self.especie}"

class Cachorro(Animal):
    def emitir_som(self):
        return "au-au!"

class Gato(Animal):
    def emitir_som(self):
        return "miau!"

o_cachorro = Cachorro("Dora", 2, "Vira-lata")
o_gato = Gato("Nino", "5 meses", "Perturbado")  # Corrigido para "5 meses"

print(o_cachorro.emitir_som())
print(o_cachorro.informacoes())
print(o_gato.emitir_som())
print(o_gato.informacoes())
