# exemplo de entrada de 10 numeros, a soma e media dos mesmos
conta = 0
condicao = True
soma = 0
while condicao:
    n1 = int(input("digite o numero "))
    conta = conta + 1
    if conta == 10:
        soma = soma + n1
        condicao = False
media = soma / 10
print(n1, end=" ")
print("media de 10 numeros é: ",media)

# fluxo valor pre determinado
# soma = 0
# n1 = 10
# n2 = 20 + 1
# for i in range(n1,n2):
#    soma = soma + i
#    print(i, end=" ")
#media = soma / 10
#print("media de 10 numeros ",media)