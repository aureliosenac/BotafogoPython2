num1 = int(input())
# inclui numero na lista e se for = 0 para sair do programa
lista =[]

while True:
    numero = int(input("digite um numero (0 - sai) : "))
    if numero == 0:
        break
    lista.append(numero)
for i in lista:    
    print(i)    