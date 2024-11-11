def somar (a, b):
    return a+b

def subtrair (a, b):
    return a-b

def multiplicar (a, b):
    return a*b

def dividir (a, b):
    return a/b

def restodiv (a, b):
    return a%b

def numeros():
    a = int(input('Qual o primeiro número?\n'))
    b = int(input('Qual o segundo número?\n'))
    return a, b

def calculadora ():
    while True:
        print('Tipos de operação: \n\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 5. Resto de divisão\n')
        operacao = input('Qual operação deseja realizar? 1/2/3/4/5\n')

        if operacao in ['1','2','3','4','5']:
            a, b = numeros()
            if operacao == '1':        
                print(f'O resultado da soma de {a} e {b} é {somar(a, b)}')
            elif operacao == '2':        
                print(f'O resultado da subtração de {a} e {b} é {subtrair(a, b)}')
            elif operacao == '3':
                print(f'O resultado da multiplicação de {a} e {b} é {multiplicar(a, b)}')
            elif operacao == '4':    
                print(f'O resultado da divisão de {a} e {b} é {dividir(a, b)}')
            elif operacao == '5':
                print(f'O resultado do resto de divisão de {a} e {b} é {restodiv(a, b)}')
            break
        else:
                print('\n-->Operação inválida, tente novamente<--\n')
                calculadora()



calculadora()