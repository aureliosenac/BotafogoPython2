# testa nota entre 0 e 10
verdade = True
while verdade:
    nota = int(input("digite nota entre 0 e 10 ")) 
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        print("nota valida ",nota)
        verdade = False           
        

