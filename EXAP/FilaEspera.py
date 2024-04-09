class FilaEspera:
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

    def retirar_apartamento(self, numero_vaga):
        if self.inicio is None:
            print("Fila de espera vazia.")
            return None

        retirado = self.inicio
        self.inicio = self.inicio.proximo
        retirado.vaga = numero_vaga
        retirado.proximo = None

        print(f"Apartamento {retirado.numero} retirado da fila de espera e recebeu a vaga {numero_vaga}.")
        return retirado

    def imprimir_fila(self):
        atual = self.inicio
        while atual:
            print(f"Apartamento {atual.numero}")
            atual = atual.proximo
