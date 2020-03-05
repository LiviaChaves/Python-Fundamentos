#MÉTODOS 
#Permitem executar ações específicas no objeto e podem também ter
#argumentos, exatamente como função.

# Criando uma lista

lst = [2,36,12,14,17,42]

# Usando um método do objeto lista

lst.append(52) #add um novo item na lista
print(lst)

# Usando um método do objeto lista

lst.count(12)

# A função help() explica como utilizar cada método de um objeto
help(lst.count)

# A função dir() mostra todos os métodos e atributos de um objeto
dir(lst)

# O método de um objeto pode ser chamado dentro de uma função, como print()

a = 'Isso é uma string'
print (a.split())
