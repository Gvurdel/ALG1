#A classe Pessoa é abstrata
#O metodo marcarPresenca da classe Pessoa é abstrato
#O atributo telefone é fracamente privado
#O atributo matricula é fortemente privado
#O metodo marcarpresenca devera incrementar o atributo presencas
#Construa um metodo asessor e um metodo modificador para o atributo matricula
#Construa um arquivo main para testar a construçao de um aluno

class Pessoa:
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.matricula = None

    def marcarPresenca(self):
        pass
    
    def matricular(self, matricula):
        self.matricula = matricula