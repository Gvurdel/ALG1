from Pessoa import Pessoa
from Cidade import Cidade


c1 = Cidade("Porto Alegre", "RS")

p1 = Pessoa("João", 1.75, c1)
p2 = Pessoa("Maria", 1.50, c1)
p3 = Pessoa("José", 1.60, Cidade("Alvorada", "RS"))

p1.imprimir()
p3.imprimir()

print("IMC de ", p1.nome, "= " , p1.getIMC(75.640))