class Pedido:
    def __init__(self):
        self.itens = {}
        self.total_a_pagar = 0.0
        self.status = "Pendente"
        
    def adicionar_item(self, item, quantidade, preco_unitario):
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade
        self.total_a_pagar += quantidade * preco_unitario
        
    def calcular_total(self):
        return self.total_a_pagar
    
    def alterar_status(self, novo_status):
        self.status = novo_status

pedido1 = Pedido()
pedido1.adicionar_item("Hamburguer", 2, 10.0)
pedido1.adicionar_item("Batata Frita", 1, 5.0)

print("Itens do pedido:")
for item, quantidade in pedido1.itens.items():
    print(f"{quantidade}x {item}")

print("Total a pagar:", pedido1.calcular_total())
print("Status do pedido:", pedido1.status)

pedido1.alterar_status("Em preparo")
print("Novo status do pedido:", pedido1.status)