from Categoria import Categoria

class Produto:
    def __init__(self, nome = None, preco = 0.0, cat = Categoria()):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.cat = cat
        
    def __str__(self):
        texto = "Produto: " + self.nome
        texto += "\nPreço: " + str(self.preco)
        texto += "\nCategoria: " + self.cat.nome
        return texto
    
