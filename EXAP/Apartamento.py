class Apartamento:
    def __init__(self, apartamento_id, numero, torre, vaga):
        self.id = apartamento_id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def cadastrar(self, lista_apartamentos):
        lista_apartamentos.append(self)
        print(f"Apartamento {self.numero} cadastrado com sucesso.")

    def imprimir(self):
        print(f"ID: {self.id}, Número: {self.numero}, Torre: {self.torre.nome}, Vaga: {self.vaga}")
