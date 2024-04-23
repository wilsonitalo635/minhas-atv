class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, quantidade):
        if quantidade < 0:
            print("A quantidade a ser atualizada deve ser um valor positivo.")
        else:
            self.estoque += quantidade
            print(f"Estoque atualizado para {self.estoque} unidades.")

    def calcular_preco_total(self, quantidade):
        if quantidade <= 0:
            print("A quantidade desejada deve ser um valor positivo.")
            return None
        elif quantidade > self.estoque:
            print("Quantidade desejada maior do que o estoque disponível.")
            return None
        else:
            preco_total = self.preco * quantidade
            return preco_total

# Uso das classes
produto1 = Produto("Camiseta", 25.0, 50)
print(f"Preço total para 10 unidades de {produto1.nome}: R${produto1.calcular_preco_total(10)}")
produto1.atualizar_estoque(20)
print(f"Preço total para 30 unidades de {produto1.nome}: R${produto1.calcular_preco_total(30)}")