class Categoria:
    def __init__(self, nome = None):
        self.id = None
        self.nome = nome
        

    def str(self):
        return "Categoria: " + self.nome
        