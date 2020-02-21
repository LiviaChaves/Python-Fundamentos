#LISTAS

listadomercado = ["ovos,farinha,leite,maçãs"] #lista de um unico elemento
print(listadomercado)

listadomercado2 = ["ovos","farinha","leite","maçãs"] #lista varios elementos
print(listadomercado2) 

print(listadomercado[0]) 
print(listadomercado2[0])

lista3=[12,100,"opashow"]
print(lista3)

#atribuindo vaçlor da lista a uma variável
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]
print(item1,item2,item3) #imprimindo

#ATUALIZANDO UM ITEM DA LISTA

print(listadomercado2)

listadomercado2[2] = "chocolate" #altera o item da posição 2 para chocolate
print(listadomercado2)

del listadomercado2[3] # deleta o item da posicão 3 da lista
print(listadomercado2)

#LISTA ANINHADAS 

#criando uma lista de listas

listas = [[1,2,3],[10,15,14],[10.1,8.7,2,3]]
print(listas)

a = listas[0] # atribui uma variável para a lista da primeira posição
print(a)

aa = a[0] # atribui uma variavel para o primeiro elemento da lista a
print(aa)

b = listas[1]
print(b)
bb = b[1]
print(bb)

#OPERAÇÕES COM LISTAS

listas2 = [[1,2,3],[6,8,4],[9.6,3.7,4.4]]
print(listas2)

w = listas2[0][0] # Atribuindo a variável w,o primeiro valor da primeira lista
print(w)

t = listas2[1][2] # Atribuindo a variável t, o terceiro valor da segunda lista
print(t)

o = listas2[0][2] + 10 #Faz uma operação de soma com o terceiro elemento da primeira lista.
print(o)

#CONCATENANDO LISTAS

lista_s1 = [8,9,6]
lista_s2 = [4,2,7]
lista_total = lista_s1 + lista_s2
print(lista_total)

#OPERADOR IN

lista_test = [12,8,23,-4]
print( 12 in lista_test) # Verifica se o valor 12 pertence a lista
print (10 in lista_test) # verifica se o valor 10 pertence a lista

#FUNÇÃO BUILT-IN

lista_bu = [9,4,3,15,28,-7,65,22]
print(lista_bu)

print(len(lista_bu)) # retorna o comprimento da lista
print(max(lista_bu)) # retorna o valor máximo da lista
print(min(lista_bu)) # retorna o menor valor da lista

lista_mercado = ["carne","leite","ovo","farinha"]
print(lista_mercado)
lista_mercado.append ("pão") # adiciona o item a lista_mercado
print(lista_mercado)
lista_mercado.append ("pão") # adiciona novamente pão no final da lista
print(lista_mercado)
lista_mercado.count("pão") # conta quantas vezes os elemento aparece na lista 

##########

v = [] # lista vazia 
print(v)
print(type(v)) # verifica o tipo da variavel 
v.append(10)
v.append(25)
v.append(7)
print(v)

##################

old_lista = [2,3,9,8]
print(old_lista)

new_lista= []
print(new_lista)

for item in old_lista:      # copia os itens de uma lista para outra
    new_lista.append(item)
print(new_lista)

cidades = ["São Paulo","Salvador","Rio de Janeiro"]
print(cidades)
cidades.extend(["Fortaleza","Palmas"]) # adiciona esses elementos a lista cidades
print(cidades)

print(cidades.index("Fortaleza")) # retorna o index da posição que o item está na lista
# Python o indice começã no zero

cidades.insert(1,"Porto Alegre") # adiciona um elemento a uma posição específica
print(cidades)

cidades.remove("Palmas") # remove um elemento da lista
print(cidades)

cidades.reverse() # reverte a lista
print(cidades)

x=[8,9,4,3,6,7]
print(x)
x.sort() # ordena a lista
print(x)