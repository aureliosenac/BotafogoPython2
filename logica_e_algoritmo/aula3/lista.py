alunos =["simone","vanessa","fernando","ricardo"] #lista
#           0         1          2         3
# turma ={"simone","vanessa","fernando","ricardo"} #set
print(alunos)
# print(turma)
print(alunos[0])
alunos[0] = "aurelio"
alunos.extend(["ferreira"])
print(alunos)
alunos.insert(0,"maria eduarda")
print(alunos)
alunos.remove("aurelio")
print(alunos)
alunos.pop()
print(alunos)
# alunos.clear() #apaga o conteudo de uma lista
alunos.sort()
print(alunos)
