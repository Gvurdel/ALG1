class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular(self):
        resultado = self.altura * self.largura 
        print(resultado)

imprimir = Retangulo(18, 16)
imprimir.calcular()



