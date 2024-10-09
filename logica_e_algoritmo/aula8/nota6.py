# programa de notas de alunos utilizando lista com dicionário
n_alunos = int(input("digite o número de alunos "))
alunos = [] # criação de lista

for i in range(n_alunos):
      nome = input("digite o nome do aluno ")
      nota1 = float(input("digite a primeira nota do aluno "))
      nota2 = float(input("digite a segunda nota do aluno "))
      media = (nota1 + nota2) / 2 #desnecessario colocar em float
      resultado = "aprovado" if media >= 6.5 else "reprovado"
      # criação do dicionário
      alunos.append(
        {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media,  
            "resultado": resultado  
        })  
      

for i in alunos:
  print(f"nome:{i["nome"]}") 
  print(f"nota1:{i["nota1"]}") 
  print(f"nota2:{i["nota2"]}") 
  print(f"media:{i["media"]}") 
  print(f"resultado:{i["resultado"]}")   

