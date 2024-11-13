def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:  # Previne divisão por zero
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def restodiv(a, b):
    if b == 0:  # Previne divisão por zero
        raise ValueError("Não é possível dividir por zero!")
    return a % b

def numeros():
    while True:
            a = float(input('Qual o primeiro número?\n'))
            b = float(input('Qual o segundo número?\n'))
            return a, b

def calculadora():
    try:
        while True:
            print('Tipos de operação: \n\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 5. Resto de divisão\n')
            operacao = input('Qual operação deseja realizar? 1/2/3/4/5\n')

            if operacao in ['1', '2', '3', '4', '5']:
                a, b = numeros()
                if not a.is_integer() or not b.is_integer():
                    raise ValueError("Por favor, insira números inteiros.")
                else:
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

    except ValueError as e:
        print(f"Erro: {e}")
        print("Tente novamente.\n")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        print("Tente novamente.\n")
    
    finally:
        # Se houver um erro ou o usuário pedir para continuar, a função chamará a si mesma
        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar == 's':
            calculadora()  # Recursão: chama novamente a função
        else:
            print("Obrigado por usar a calculadora! Até logo!")

# Chama a função da calculadora
calculadora()
