from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def imprimir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo}, Portas: {self._portas}")
