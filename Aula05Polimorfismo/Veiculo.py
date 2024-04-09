from Categoria import Categoria

class Veiculo:
    def __init__(self, marca, ano, cat=Categoria(None)):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.categoria = cat

    def imprimir(self):
        print("Marca: " , self.marca)
        print("Ano: " , self.ano)
        print("Categoria: " , self.categoria)