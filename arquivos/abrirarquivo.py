""" 
r - read
a - append - inserir registro
w - write escrita
x - criar arquivo
rw - leitura e escrita
"""
#open("Caminho", "modo de abertura")
arquivo = open("C:\Users\47129532024.4\Desktop\arquivos\texto.txt","r")
print(arquivo.readable())
# imprimir od dados do arquivo chamado arquivo
print(arquivo.read())