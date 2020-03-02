if 5 > 2:  #caso a condição estiver correta imprime o print abaixo
    print("Python funcional!")
 

if 5 < 2:  #caso a condição estiver correta imprime o print abaixo
    print("Esta certo")
else: # SeNão imprime o print abaixo
    print("Esta errado")    

print(3>2)

if 5 == 5:
    print("Testando")

if 4 > 3:
    print("Tudo funcional")

############################################
 
# CONDICIONAIS ANINHADOS

idade = 18
nome = 'Bob'

if idade > 17:
    print('Você pode dirigir')
else:
    print('Você não pode dirigir')    

if idade > 13:
    if nome == 'Bob':
        print('Você ṕde entrar')
    else:
        print('Vocẽ não pode entrar')

idade2 = 21
nome2 ='Jose'

if idade2 >=21 and nome2 == 'Jose': # condição que se a idade e o nome forem correspondentes as da variaveis ele executa o print
    print("Você pode entrar")

if (idade2 >=21) or (nome2 == 'Jose'): # condição que se a idade ou o nome forem correspondentes as da variaveis ele executa o print
    print("Você pode entrar")

####################################

#ELIF
        
dia = 'Terça'

if(dia == 'Segunda'):  #SE
    print('Hoje fará sol')
else:  #SENÃO
    print('Hoje vai chover')

if(dia =='Segunda'):  #SE
    print("Hoje fará sol")
elif (dia == "Terça"): #Evita escrever varios ifs 
    print("Hoje vai chover")
else: #SENÃO
    print ("Sem previsão para o dia selecionado") 

###############################################################

dis = input('Digite o nome da disciplina: ') #recebe um valor digitado pelo usuario
nota_final = input('Digite a nota final (Entre 0 e 100): ') #recebe um valor digitado pelo usuario

if (dis == 'Gepgrafia') and (nota_final >= '70' ):
    print('Aprovado')
else:
    print('Reprovado')    

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final)) #coloca displina no lugar de %s e nota_final no lugar de %r
else:
    print('Lamento, acho que você precisa estudar mais!')


