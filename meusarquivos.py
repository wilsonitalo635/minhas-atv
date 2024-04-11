class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def qual_nome(self, novo_nome):
         self.nome = novo_nome
    def obter_nome(self):
        return self.nome
    def qual_idade(self, nova_idade):
        self.idade = nova_idade
    def obter_idade(self):
        return self.idade
    def qual_altura(self, nova_altura):
        self.altura = nova_altura
    def obter_altura(self):    
        return self.altura
    def mensagem(self, nova_mensagem): 
        return f"{self.nome} oi, td bem com vc?"
    def mensagem2(self, nova_mensagem):
        return f"{self} n, minha cabeça está borbulhando"
if __name__ == "__main__":
    pessoa1 = Pessoa("Pedro","17", "1.71")
    print("Nome:", pessoa1.obter_nome())
    print("Idade:", pessoa1.obter_idade())
    print("Altura:", pessoa1.obter_altura())
    print("Mensagem:", pessoa1.mensagem("oi, td bem com vc?"))
    print("Mensagem2:", pessoa1.mensagem("n, minha cabeça está borbulhando"))






