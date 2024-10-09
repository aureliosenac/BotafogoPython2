# calcula notas de 50, 10 e 1
resposta ='S'

while resposta == 'S':
    valor =int(input('qual valor para saque '))
    n50 = valor // 50
    r50 = valor % 50
    n10 = r50 // 10
    n1 = r50 % 10

    print('notas de 50 ', n50)
    print('notas de 10 ', n10)
    print('moedas de 1 ', n1)
    resposta = input('deseja fazer outro saque (s/n)? ')
    
