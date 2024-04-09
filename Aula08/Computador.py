class Computador():

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}"
    
    
    def cadastrar(self):
        
        pass