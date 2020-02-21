#ESTRUTURA DE DADOS TUPLAS

#criando uma tupla
tupla = ("Geografia",23,"Elefante")
print(tupla)

# tupla.append("Chocolate") Erro, Tuplas não suportam append
# del tupla["Elefante"] Erro, Tuplas não suportam delete de um item especifico

tupla2 = ("Chocolate")
print(tupla2)

print(tupla[0]) #imprimindo  um item da tupla

len(tupla) # verificando o comprimento da tupla

print(tupla[1:]) #Slicing, da mesma forma que se faz na lista (retorna todos elementos a partir da posição 1)

print(tupla.index('Elefante')) # retorna a posição do elemento 

# tupla[1] = 21 Tuplas não suportam atribuição de item

del tupla # deleta a tupla

tupla3 = ('A','B','C')
print(tupla3)

# tupla3[0] = 'D' Tuplas não suportam atricuição de item

listaTupla = list(tupla3) # Converte a Tupla em uma lista
print(listaTupla) 

listaTupla.append('D') # add um item a lista
print(listaTupla) 

tupla4 = tuple(listaTupla)
print(tupla4)