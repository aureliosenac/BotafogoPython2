# solicito o usuário para digitar um número
numero = int(input("digite um numero para tabuada de 10 "))
for index in range (10):
    aux = index * numero
    print(index ,"x", numero ," = ",aux)