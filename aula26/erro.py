def cadastrar_cliente():
    while True:
        try:
            nome = input("Digite o nome do cliente: ")
            if not nome.isalpha():
                raise ValueError("O nome deve conter apenas letras.")
            
            idade = int(input("Digite a idade do cliente: "))
            if idade < 0 or idade > 120:
                raise ValueError("A idade deve estar entre 0 e 120.")
            
            email = input("Digite o email do cliente: ")
            if "@" not in email or "." not in email.split("@")[-1]:
                raise ValueError("Email inválido. Certifique-se de que está no formato correto.")
            
            print("\nCadastro realizado com sucesso!")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Email: {email}")
            break
        
        except ValueError as e:
            print(f"Erro: {e}")
            print("Tente novamente.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            print("Tente novamente.\n")

# Executa o cadastro
cadastrar_cliente()
