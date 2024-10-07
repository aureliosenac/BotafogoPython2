# Encontra valores de A e C
def valor_fim_AeC(a1, b1):
    c = 0
    while a1 > b1:
        resultado = b1 - a1
        a1 = resultado
        c += 1
    print("valor de c: ",c)
    print("valor de a: ",a1)    

for i in range(3):
    if i == 0:
        a = 10 ; b = 2
    if  i == 1:
        a = 6  ; b = 2
    if i == 2:
        a = 15 ; b = 3
    valor_fim_AeC(a,b)                   



