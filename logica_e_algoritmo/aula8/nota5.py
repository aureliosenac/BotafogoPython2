# calculando notas de alunos utilizando while
n_alunos = int(input("digite o número de alunos "))
i = 0
while i < n_alunos:
    aluno = input("digite o nome do aluno ")
    nota1 = float(input("digite a primeira nota do aluno "))
    nota2 = float(input("digite a segunda nota do aluno "))
    media = (nota1 + nota2) / 2 #desnecessario colocar em float
    if media >= 6.5:
        print("o ",aluno," foi aprovado - media ",media)
    else:
        print("o ",aluno," foi reprovado - media ",media)
    i = i + 1    