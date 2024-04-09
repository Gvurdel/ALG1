from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, ano, cat, qtdPortas):
        super().__init__(marca, ano, cat)
        self.qtdPortas = qtdPortas

    def imprimir(self):
        super().imprimir()
        print("Portas: " , self.qtdPortas)