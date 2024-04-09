from Cidade import Cidade

class Pessoa:
    def __init__(self, nome, altura, city):
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = city


    def __str__(self):
        texto = "Nome: " + self.nome
        texto += "\nAltura: " + str(self.altura)
        texto += "\nCidade: " + self.cidade.nome 
        texto += "\nEstado: " + self.cidade.uf 
        return texto


    def imprimir(self):
        print("Nome: ", self.nome)
        print("Altura: ", self.altura)
        self.cidade.imprimir()

    def getIMC(self, peso):
        return peso / (self.altura * self.altura)
    

