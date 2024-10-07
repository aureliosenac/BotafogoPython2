preco = float(input("digite o preço da mercadoria "))
p_desconto = float(input("digite o desconto da mercadoria "))
desconto = preco * p_desconto / 100
novopreco = preco - desconto
print("desconto  - R$ ", desconto)
print("novopreco - R$ ", novopreco)