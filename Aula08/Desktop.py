from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.__potenciaDaFonte = potenciaDaFonte
    
    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Potência da Fonte: {self.__potenciaDaFonte}"
    
    def cadastrar(self):
        
        # Implemente aqui a lógica específica de cadastro para Desktop
        pass