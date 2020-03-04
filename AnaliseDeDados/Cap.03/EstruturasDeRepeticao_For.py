#CRIANDO UMA TUPLA E IMPRIMINDO CADA UM DOS VALORES
tp = (2,9,6)
for i in tp: 
    print(i) 

#CRIANDO UMA LISTA E IMPRIMINDO CADA UM DOS VALORES
Lista = ["leite","frutas","carnes"]
for i in Lista:
    print(i)

#IMPRIMINDO VALORES ENTRE 0 E 5
for contador in range(0,5):
    print(contador)

#IMPRIMINDO OS NUMEROS PARES
ListaNum = [1,2,3,4,5,6,7,8,9,10]
for num in ListaNum: #Percorre todos os números da lista e imprime somente aqueles que são pares
    if num % 2 == 0:
        print(num)


# Listando os números no intervalo entre 0 e 101, com incremento em 2
for i in range(0,101,2):  
    print(i)


# Strings também são sequências
for caracter in 'Python é uma linguagem de programação divertida!':
    print (caracter)

#LOOPS ANINHADOS

for i in range (0,5): #range(conjunto de valores)
    for a in range(0,5):
        print(a)         

#Operando os valores de uma lista com loop for

listaB = [63,25,12,32,84,14,35,11,18]
soma = 0
for i in listaB: #percorre a lista e
    double_i = i * 2 # para cada item (i) da lista multiplica o item por dois e grava na variavel
    soma += double_i # soma a variovel soma com os valores da variavel double_i
print(soma)  

#Loops em lista de listas

listas = [[1,2,3],[10,15,14],[10.1,8.6,8.9]]
for valor in listas: #percorre cada valor do objeto(listas)
    print(valor)

#Contando os itens de uma lista    

listaC = [3,9,5,6,7,1]
count = 0
for item in listaC:
    count += 1 #conta a quantidade de elementos da lista
print(count)    

#Contando o numero de colunas

lstCol = [[2,9,36],[33,37,25],[8,21,29]]    
primeira_linha = lstCol[0] #primeira posição da lista
count = 0
for column in primeira_linha: #percorre a primeira lista das listas
    count = count + 1
print(count)    

# Pesquisando em listas

listaP = [9,5,7,35,12]
for item in listaP: #percorre os itens da lista
    if item == 35:
        print("Numero encontrado na lista")

#listando as chaves de um dicionário

dict = {'k1':'Python','k2':'R','k3':'Scala'}
for item in dict:
    print(item)


# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os 
# itens de um dicionário
for k,v in dict.items(): #retorna chave e valor
    print (k,v)    