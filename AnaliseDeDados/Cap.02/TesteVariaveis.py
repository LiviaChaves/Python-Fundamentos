#Testar baixando o mateiral do curso e utilizar o jupyter

var_teste = 1
print(var_teste) # imprime o valor da variável.

var_teste = 2
print(var_teste) # imprime o valor 2
print(type(var_teste))  #mostra o tipo da variável

var_teste = 9.5
print(var_teste)  #imprime o valor 9.5
print(type(var_teste)) #mostra p tipo da variável

x = 1
print(x)#imprime o valor 1
print(type(x)) #mostra o tipo da variável

#DECLARAÇÃO MULTIPLA

pessoa1, pessoa2,pessoa3 = "Maria", "José","Tobias"
print(pessoa1) #imprime Maria
print(pessoa2) # Imprime José
print(pessoa3) # Imprime Tobias 

fruta1 = fruta2 = fruta3 = "Laranja" # as tres variáveis imprime Laranja
print(fruta1)
print(fruta2)
print(fruta3)

#Variáveis atribuidas a outras váriaveis e ordem dos operadores?

largura = 2
altura = 4
area = largura * altura
print(area)

perimetro = 2 * largura + 2 * altura
print(perimetro)

perimetro = 2 * (largura + 2) * altura #ordem  dos operadores é a mesmas seuidas na matematica
print(perimetro)

#Operação

idade1=25
idade2=33

print(idade1+idade2)
print(idade1-idade2)
print(idade1*idade2)
print(idade2/idade1)
print(idade1%idade2)

#Concatenação de variáveis:

nome= "Livia"
sobrenome="Chaves"
fullNome= nome + ' ' + sobrenome #uni duas strings
print(fullNome)