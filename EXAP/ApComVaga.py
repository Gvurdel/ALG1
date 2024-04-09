from Apartamento import Apartamento

class ApComVaga:
    def __init__(self):
        self.inicio = None

    def adicionar_apartamento(self, apartamento):
        if self.inicio is None: 
            self.inicio = apartamento
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = apartamento

    def imprimir_lista(self):
        atual = self.inicio
        while atual:
            print(f"Apartamento {atual.numero}, Torre: {atual.torre.nome}, Vaga: {atual.vaga}")
            atual = atual.proximo