class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
    def mostrar_informacoes(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.num_paginas)
        
    def calcular_palavras_por_pagina(self):
        # Considerando uma média de 275 palavras por página
        return 275

def solicitar_informacoes_livro():
    titulo = input("Insira o título do livro: ")
    autor = input("Insira o nome do autor do livro: ")
    num_paginas = int(input("Insira o número de páginas do livro: "))
    return Livro(titulo, autor, num_paginas)

def main():
    livro = solicitar_informacoes_livro()
    livro.mostrar_informacoes()
    palavras_por_pagina = livro.calcular_palavras_por_pagina()
    print("Quantidade de palavras por página:", palavras_por_pagina)

if __name__ == "_main_":
    main()