# calcula o custo de cada caneta
n_canetas = 30
valor_nota = 100.00
troco = 67.00
valor_compra = valor_nota - troco
valor_caneta = valor_compra / n_canetas
print("o valor de cada caneta é: R$ {:.2f}".format(valor_caneta))