conta = 1
soma = 0
import math
lista=[]
while conta != 0:
    num1 = int(input("digite número inteiro - para encerrar digite 0 "))
    if num1 == 0 and soma == 0:
        break
    if num1 != 0:
        # lista.append(num1)
        conta += 1 
        soma = soma + num1
    else:    
        conta = conta - 1
        media = math.ceil(soma / conta) #arredonda para cima
        print("quantidade de números ",conta)
        print("media aritmética ",media)
        conta = 0