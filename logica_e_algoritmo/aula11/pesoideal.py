# calcula o peso ideal para homens e mulheres
sexo = input("digite o sexo - M ou F ")
altura = float(input("digite a altura "))
if sexo == "M":
    peso = (72.7 * altura) - 58 
    print(f"peso ideal masculino {peso:.2f}")
else:
    peso = (62.1 * altura) - 44.7
    print(f"peso ideal feminino {peso:.2f}")
  
