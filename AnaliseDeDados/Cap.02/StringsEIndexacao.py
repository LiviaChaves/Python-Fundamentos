# Em Python, a INDEXAÇÃO COMEÇA POR 0

texto="Python e Análise de Dados"
 #texto[0] = P
 #texto[1] = y
 #texto[2] = t
print ('Testando Strings em Python')
print ('Testando \nStrings \nem \nPython') #Quebra de linha 

#INDEXAÇÃO

s = "Ola mundo"
print(s)

s[0]
s[1]
s[2]

# Pode ser Usado : para executar um slicing que faz a leitura ate
#um ponto desligado

print(s[1:]) #retorna apartir do posição 1
print(s[:3]) #retorna tudo até a posição 3
print(s[:]) # retorna a frase interia
print(s[-1]) # retorna tudo de trás para frente
print(s[:-1]) # retorna tudo menos a ultima letra

#Nós também podemos usar a notação de índice e fatiar a 
#string em pedaços específicos (o padrão é 1). 
#Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, 
#um número que especifica a frequência para retornar elementos

print(s[::1])
print(s[::2])#retorna os caractera saltando 2 posições
print(s[::-1])#retorna saltando 1 posição de trás para  frente

#PROPRIEDADE de String

d = 'Data Science Academy'
#Dar errp: s[0] = 'x'

# Concatenando strings
d = d + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
print(d)

letra = 'w'
print(letra * 3) # Podemos usar o símbolo de multiplicação para criar repetição
print(letra)

#Funções Built-in de Strings
print(d)
print (d.upper()) #deixa tudo maiúsculo 
print (d.lower()) # deixa tudo minúsculo
print (d.split())  #dividi por espaçãos em branco(padrão)
print (d.split('y')) # dividi por um por um elemento específico 

#FUNÇÕES STRING

f = 'seja bem vindo ao universo de python'
print(f)

print (f.capitalize()) # transforma a primeira letra em maiúsculo
print (f.count('a')) #conta quantas vezes o caractere aparece
print (f.find('p')) # encontra uma determinada letra
print (f.islower()) # retorna true se a string for minúscula
print (f.isspace()) # retorna true se a string for espaço
print (f.endswith('o')) #verifica se 'O' é a ultima letra

#COMPRANDO STRINGS

print("Python" == "R")
print("Python" == "Python")