"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas"""
distancia = float(input("digite a distancia em km "))
if distancia <= 200:
    preco = float(distancia * 0.50)
else:
    preco = float(distancia * 0.45)
print("valor da viagem - R$", preco)    

