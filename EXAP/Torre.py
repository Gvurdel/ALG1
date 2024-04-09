class Torre:
    def __init__(self, torre_id, nome, endereco):
        self.id = torre_id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self, lista_torres):
        lista_torres.append(self)
        print(f"Torre {self.nome} cadastrada com sucesso.")

    def imprimir(self):
        print(f"ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}")