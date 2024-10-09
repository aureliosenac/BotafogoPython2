# calculando nota de alunos com o for
n_alunos = int(input("digite o número de alunos "))
for i in range(n_alunos):
    aluno = input("digite o nome do aluno ")
    nota1 = float(input("digite a primeira nota do aluno "))
    nota2 = float(input("digite a segunda nota do aluno "))
    media = (nota1 + nota2) / 2 #desnecessario colocar em float
    if media >= 6.5:
        print("o ",aluno," foi aprovado - media ",media)
    else:
        print("o ",aluno," foi reprovado - media ",media)    