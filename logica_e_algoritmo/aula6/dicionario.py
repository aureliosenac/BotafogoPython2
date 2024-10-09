"""
Dicionario possui chave valor 
quando passo a chave, ele me devolve o valor,
não aceita valores duplicados,
é mutável, podemos modificar o valor dele """

meses = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Mai":"Maio",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro",
      
    
     }
#imprimir todo dicionario
print(meses)
#imprimir o valor a partir de uma chave
#passei uma chave e ele retorna o valor da respectiva chave
print(meses["Jan"])
print(meses["Jun"])
#print(meses["gato"]) keyError: 'gato'
