# calcula notas 50,10 e 1 e futuramente centavos
def calcula_notas(valor):

    notas50 = 0; notas10 = 0; notas1 = 0; auxvalor = valor
    
    notas50 = valor // 50 #divide por 50 (valor)
    valor = notas50 % 50 # restante da divisão por 50
    notas10 = valor // 10 # divide por 10 (valor)
    valor = notas10 % 10  # restante da divisao por 10
    notas1 = valor  #divide por 1 (valor inteiro)
    centa50 = str(auxvalor)
    centavos50 = centa50[-2]
    centa25 
    centavos25 
    centavos10
    centavos05

    if notas50 != 0:
        print("notas de R$ 50 " ,notas50)
    if notas10 != 0:
        print("notas de R$ 10 ", notas10)
    if notas1 != 0:    
        print("notas de R$ 1 ", notas1)


    return 
# moedas .50 .25 .10 .05


valor_conta = float(input("digite o valor da conta: "))
print("valor da conta R$ ",valor_conta)
calcula_notas(valor_conta)
