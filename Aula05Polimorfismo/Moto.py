from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, ano, cat, cilindradas):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilindradas

    def imprimir(self):
        super().imprimir()
        print("Cilindradas: " , self.cilindradas)