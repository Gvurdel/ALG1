class PilhaVeiculos:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self):
        if self.veiculos:
            return self.veiculos.pop()
        else:
            print("A pilha está vazia.")

    def imprimir_pilha(self):
        for veiculo in self.veiculos:
            veiculo.imprimir_informacoes()
