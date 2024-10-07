# calcula notas 50,10 e 1
def calcula_notas(valor):
    notas50 = 0; notas10 = 0; notas1 = 0
    
    notas50 = valor // 50 #divide por 50 (valor inteiro)
    valor %= 50 # restante da divisão por 50
    notas10 = valor // 10 # divide por 10 (valor inteiro)
    valor %= 10  # restante da divisao por 10
    notas1 = valor  #divide por 1 (valor inteiro)
    if notas50 != 0:
        print("notas de R$ 50 " ,notas50)
    if notas10 != 0:
        print("notas de R$ 10 ", notas10)
    if notas1 != 0:    
        print("notas de R$ 1 ", notas1)
    return 



valor_conta = int(input("digite o valor da conta: "))
print("valor da conta R$ ",valor_conta)
calcula_notas(valor_conta)



