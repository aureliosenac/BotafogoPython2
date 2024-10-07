# programa de cadastro de pessoas

verdade = True
while verdade:
    erro = 0
    nome = input("digite o seu nome ")
    idade = int(input("digite a sua idade "))
    salario = float(input("digite o seu salário "))
    sexo = input("digite o sexo - f ou m ")
    civil = input("digite estado civil - s | c | v | d ")
    if len(nome) < 3:
        print("nome invalido")
        erro = 1
    if idade < 0 and idade > 150:
        print("idade inválida")
        erro = 1
    if salario == 0:
        print("salário invalido") 
    if  sexo != "f" and sexo != "m":
        print("sexo invalido")
        erro = 1
    if civil != "s" and civil != "c" and civil != "v" and civil != "d":   
        print("estado civil inválido")
        erro = 1
    if erro == 0:
        verdade = False
        print("cadastro ok")
