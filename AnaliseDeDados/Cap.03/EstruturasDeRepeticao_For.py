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