from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Tempo de Bateria: {self.__tempoDeBateria}"
    
    def cadastrar(self):
        # Implemente aqui a lógica específica de cadastro para Notebook
        pass