try:
    n1 = int(input("digite o primeiro número "))
    print(n1)
    n2 = int(input("digite o primeiro número "))
    print(n2)
    calculo = n1 / n2
    print("resultado da divisão ",calculo)

except ValueError:  
    print("digite um valor numérico")  

except ZeroDivisionError:  
    print("não é possível dividir por zero")  

except:
    print("erro inesperado")


finally:    
    print("------")
    print("sempre executará... entrando ou não dentro de uma exceção. ")
    print("안녕하세요")