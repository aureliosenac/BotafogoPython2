# Classe base para uma conta bancária
class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
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
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")

# Classe filha para incluir transferências
class ContaCorrente(ContaBancaria):
    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")

# Demonstração de uso
if __name__ == "__main__":
    # Criando duas contas para simular operações
    # conta1 = ContaCorrente("João", "12345-6", saldo=1000)
    # conta2 = ContaCorrente("Maria", "65432-1", saldo=500)
    conta1 = ContaCorrente(input("digite o nome do titular "), 
                           int(input("digite a conta corrente ")),saldo=1000)
    conta2 = ContaCorrente("Maria", "65432-1", saldo=500)


    # Operações básicas
    conta1.exibir_saldo()
    conta1.sacar(int(input("digite o valor a sacar ")))
    conta1.exibir_saldo()
    conta1.depositar(int(input("digite o valor a depositar ")))

    # Transferência
    conta1.transferir(int(input("digite o valor a transferir para conta2 ")), conta2)
    conta1.exibir_saldo()
    conta2.exibir_saldo()
