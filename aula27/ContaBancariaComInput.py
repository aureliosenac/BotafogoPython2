# Classe base para uma conta bancária
class ContaBancaria:
    def __init__(self, titular, numero_conta, senha, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")

# Classe filha para incluir transferências
class ContaCorrente(ContaBancaria):
    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.titular} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")

# Função para autenticar o usuário
def autenticar_usuario(conta):
    senha_informada = input("Digite a senha para acessar sua conta: ")
    if senha_informada == conta.senha:
        print(f"Bem-vindo, {conta.titular}!")
        return True
    else:
        print("Senha incorreta. Tente novamente.")
        return False

# Função para gerenciar as transações
def realizar_transacao(conta):
    while True:
        print("\nEscolha a transação que deseja realizar:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Exibir saldo")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$"))
            conta.depositar(valor)
        
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$"))
            conta.sacar(valor)
        
        elif opcao == "3":
            numero_conta_destino = input("Digite o número da conta destino: ")
            valor = float(input("Digite o valor da transferência: R$"))
            conta_destino = encontrar_conta(numero_conta_destino)
            if conta_destino:
                conta.transferir(valor, conta_destino)
            else:
                print("Conta destino não encontrada.")
        
        elif opcao == "4":
            conta.exibir_saldo()
        
        elif opcao == "5":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para encontrar a conta pelo número da conta
def encontrar_conta(numero_conta):
    # Procurando contas criadas no sistema (como exemplo)
    if numero_conta == "12345-6":
        return conta1
    elif numero_conta == "65432-1":
        return conta2
    elif numero_conta == "12765-9":
        return conta3
    else:
        return None

# Função para cadastro de novo usuário
def cadastrar_usuario():
    print("\nCadastro de novo usuário!")
    nome = input("Digite seu nome: ")
    numero_conta = input("Digite o número da sua conta: ")
    senha = input("Digite uma senha para sua conta: ")
    saldo_inicial = float(input("Digite o saldo inicial (ou 0 para nenhum depósito): R$"))
    
    # Criando a conta com os dados informados
    conta = ContaCorrente(nome, numero_conta, senha, saldo_inicial)
    
    # Adicionando a conta ao sistema
    contas[conta.numero_conta] = conta
    print(f"Conta criada com sucesso! Bem-vindo(a), {nome}!")

# Função para seleção de conta ou criação de nova
def selecionar_ou_cadastrar():
    while True:
        print("\nSelecione uma opção:")
        print("1. Usar conta existente")
        print("2. Criar uma nova conta")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            numero_conta = input("Digite o número da conta: ")
            conta = encontrar_conta(numero_conta)
            if conta:
                print(f"Conta encontrada! Bem-vindo(a), {conta.titular}!")
                if autenticar_usuario(conta):
                    realizar_transacao(conta)
                    break
            else:
                print("Conta não encontrada. Tente novamente.")
        
        elif opcao == "2":
            cadastrar_usuario()
            # Após cadastro, o usuário pode acessar sua conta
            numero_conta = input("Digite o número da conta criada: ")
            conta = encontrar_conta(numero_conta)
            if conta:
                if autenticar_usuario(conta):
                    realizar_transacao(conta)
                    break
        else:
            print("Opção inválida. Tente novamente.")

# Demonstração de uso
if __name__ == "__main__":
    # Criando um dicionário para armazenar as contas
    contas = {}

    # Criando algumas contas iniciais para simular o sistema
    conta1 = ContaCorrente("João", "12345-6", "senha123", saldo=1000)
    conta2 = ContaCorrente("Maria", "65432-1", "senha456", saldo=500)
    conta3 = ContaBancaria("Carlos", "12765-9", "senha789", saldo=300)

    # Adicionando as contas ao sistema
    contas[conta1.numero_conta] = conta1
    contas[conta2.numero_conta] = conta2
    contas[conta3.numero_conta] = conta3

    # Seleção de usuário: usar conta existente ou criar nova
    print("Bem-vindo ao sistema bancário!")
    selecionar_ou_cadastrar()
