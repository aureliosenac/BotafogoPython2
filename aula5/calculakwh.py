print("para instalação residencial digite ", "R")
print("para instalação industrial  digite ", "I")
print("para instalação comercial   digite ", "C")
kwh = float(input("digite a quantidade kwh "))
instalacao = input("digite o tipo da instalação ")

if instalacao == "R" or instalacao == "r":
    tipo = "residendial"
    if kwh <= 500:
       preco = 0.40
    else:
       preco = 0.65   
elif instalacao == "C" or instalacao == "c":
    tipo = "comercial"
    if kwh <= 1000:
       preco = 0.55
    else:
       preco = 0.60
elif instalacao == "I" or instalacao == "i":
    tipo = "industrial"
    if kwh <= 5000:
       preco = 0.70
    else:
       preco = 0.80 
else:
    preco = 0
    tipo = " "
    print("erro ! tipo de instalação desconhecida")
    custo = kwh * preco
print("preço de consumo ",tipo," R$ ",custo)




