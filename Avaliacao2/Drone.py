from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, helices):
        super().__init__(marca, modelo)
        self.__helices = helices

    def imprimir_informacoes(self):
        print(f"Drone: {self.marca} {self.modelo}, Hélices: {self.__helices}")
        
        
