#ao executar o set, o resultado é sempre diferente
#não consigo buscar por indice

frutas = {"maças","laranja","banana","pera","uva","uva"}

print(frutas)
print("-------")
# adicionar
frutas.add("melão")
print(frutas)
#remover pelo conteúdo
frutas.remove("uva")
print(frutas)
print("*****")
frutas.pop() # último da lista
print(frutas)
frutas.pop()
print(frutas)
print("-------")
# o pop remove o último item da lista ou set, porém como
# o set não é ordenado, nunca sabemos quem é o último item da lista

conjunto1 = {"maça","uva","ameixa"}
conjunto2 = {100,200,300}
conjunto3 = {True,False,False,True}
conjunto4 = {"simone","Rua a","Iraja",21980831997,54,"Pós Graduação"}
print(conjunto1)
print("-------")
print(conjunto2)
print("-------")
print(conjunto3)
print("-------")
print(conjunto4)
