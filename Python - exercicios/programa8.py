
# Inicializa uma lista vazia
numeros = []
soma = 0
# Loop para coletar 5 números
for i in range(1,6):
    # Pede ao usuário para inserir um número
    numero = float(input(f"Digite o {i}º número: ")) 
    # Adiciona o número à lista
    numeros.append(numero)
    soma += numero
    
media = soma / 5
# Exibe a lista de números
print("Os números inseridos foram:", numeros)
# exibe o maior numero
print("soma: ",soma)
print("media: ",media)

    