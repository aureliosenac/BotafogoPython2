# operação aritmética
print("digite o número da operação que deseja realizar")
print("1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão")
operacao1 = int(input())
num1 = float(input("digite o primeiro número "))
num2 = float(input("digite o segundo número "))
if operacao1 == 1:
    resultado = num1 + num2
    operacao2 = "soma"
if operacao1 == 2:
    resultado = num1 - num2
    operacao2 ="subtração"
if operacao1 == 3:
    resultado = num1 * num2
    operacao2 = "multiplicação"
if operacao1 == 4:
    resultado = num1 / num2
    operacao2 = "divisão"   
print("o resultado da ",operacao2, "é ",resultado)      

