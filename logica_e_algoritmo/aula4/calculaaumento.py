"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%."""
salario = float(input("digite o salario "))
teto_salario = float(1250)

if salario <= teto_salario:
    aumento1 = (salario * 15) / 100
    novo_salario = salario + aumento1
else:
    novo_salario = salario * 1.1
print("salario anterior: R$ ", salario)
print("novo salario    : R$ ", novo_salario) 
