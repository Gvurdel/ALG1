from Pessoa import Pessoa
from AlunoGraduacao import AlunoGraduacao

pessoa = Pessoa(id=1, nome="João", telefone="99999999")
pessoa.matricular("202301")

aluno = AlunoGraduacao(id=2, nome="Maria", telefone="88888888", matricula="202302")
    
aluno.marcarPresenca()
print(f"ID Pessoa: {pessoa.id}")
print(f"Nome Pessoa: {pessoa.nome}")
print(f"Telefone Pessoa: {pessoa.telefone}")
print(f"Matrícula Pessoa: {pessoa.matricula}")

print(f"ID Aluno: {aluno.id}")
print(f"Nome Aluno: {aluno.nome}")
print(f"Telefone Aluno: {aluno.telefone}")
print(f"Matrícula Aluno: {aluno.matricula}")
print(f"Presenças Aluno: {aluno.presencas}")