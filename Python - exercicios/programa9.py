# números impares
# Inicializa uma lista vazia
numeros = []

# Loop para coletar 5 números
print("números impares")
for i in range(50):
    # Pede ao usuário para inserir um número
    numero = int(i) 
    # Adiciona o número à lista
    numeros.append(numero)
    
    if  numero % 2 != 0:
        print(numero, end=" ")
