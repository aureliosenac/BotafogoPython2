# testa nome e senha do usuario
verdade = True
while verdade:
    nome = input("digite o seu nome ")
    senha = input("digite uma senha ")
    if senha == nome:
        print("nome e senha iguais - repita a operacao ")
    else:
        print("cadastro ok") 
        verdade = False       
        
        

