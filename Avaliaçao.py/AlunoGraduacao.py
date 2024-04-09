from Pessoa import Pessoa

class AlunoGraduacao(Pessoa):
    def __init__(self, id, nome, telefone, matricula):
        super().__init__(id, nome, telefone)
        self.matricula = matricula
        self.presencas = 0

    def matricular(self, matricula):
        self.matricula = matricula