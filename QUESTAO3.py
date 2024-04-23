class Conta_bancaria:
    def __init__(self, num_conta, saldo, nome_titular):
        self.num_conta = num_conta
        self.saldo = saldo
        self.nome_titular = nome_titular

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso! Novo saldo: {self.saldo}")
        else:
            print("O valor do depósito deve ser maior que zero!!")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de {valor} realizado com sucesso! Novo saldo: {self.saldo}")
            else:
                print("Saldo insuficiente para fazer o saque!")
        else:
            print("O valor do saque deve ser maior que zero!!")

    def mostrar_saldo(self):
        print(f"Mostrar saldo atual: {self.saldo}")

# Uso das classes
conta_dalulu = Conta_bancaria("1234567", 10000, "Wilson e Pedro")
conta_dalulu.depositar(125)
conta_dalulu.sacar(400)
conta_dalulu.mostrar_saldo()
