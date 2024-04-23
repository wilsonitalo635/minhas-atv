class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def definir_nome(self, novo_nome):
        self.nome = novo_nome

    def definir_idade(self, nova_idade):
        self.idade = nova_idade

    def definir_altura(self, nova_altura):
        self.altura = nova_altura

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return self.altura

    def cumprimentar(self):
        return f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e minha altura é {self.altura}m."

pessoa1 = Pessoa("Wilson", 17, 1.63)
print(pessoa1.cumprimentar())

pessoa2 = Pessoa("Pedro", 20, 1.53)
print(pessoa2.cumprimentar())