
# Inicializa uma lista vazia
numeros = []

# Loop para coletar 5 números
for i in range(5):
    # Pede ao usuário para inserir um número
    numero = float(input(f"Digite o {i+1}º número: ")) 
    # Adiciona o número à lista
    numeros.append(numero)
# encontra o maior número da lists    
maior_numero = max(numeros)
# Exibe a lista de números
print("Os números inseridos foram:", numeros)
# exibe o maior numero
print("maior numero ",maior_numero)

