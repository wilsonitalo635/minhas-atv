class Carro:
    def __init__(self, carro, modelo, ano, cor):
        self.carro = carro
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado!!")
        else:
            print("O carro já está ligado!!")
            
    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado!!")
        else:
            print("O carro já está desligado!!")
            
    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade 
            print(f"O carro acelerou para {self.velocidade} km/h")
        else:
            print("O carro precisa estar ligado para acelerar")
            
# Uso das classes
dados_carro = Carro("Porsche", "Porsche 911", "1963", "prata")
dados_carro.ligar()
dados_carro.acelerar(60)
dados_carro.desligar()
