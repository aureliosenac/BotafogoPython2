# programa de notas de alunos utilizando dicionário
alunos = {} #criando dicionario de alunos
n_alunos = int(input("digite o número de alunos "))
import sys # importando biblioteca com função de exit
if n_alunos == 0:
    print("programa cancelado")
    sys.exit() # exit no programa
for i in range(n_alunos):
    nome = input("digite o nome do aluno ")
    #i = i + 1
    nota1 = float(input("digite a 1a nota do aluno "))
    nota2 = float(input("digite a 2a nota do aluno "))
    media = (nota1 + nota2) / 2
    alunos[nome] = {"nota1":nota1,
                    "nota2":nota2,
                    "media":media}
print("\n Notas dos alunos:")
for nome, dados in alunos.items():
    print(f"Nome:{nome}")
    print(f"Nota1:{dados["nota1"]}")
    print(f"Nota2:{dados["nota2"]}")
    print(f"Média:{dados["media"]}")
    print()