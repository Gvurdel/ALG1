class Cidade:
    def __init__(self, nome, estado):
        self.id = None
        self.nome = nome
        self.uf = estado

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Estado: ", self.uf)
        