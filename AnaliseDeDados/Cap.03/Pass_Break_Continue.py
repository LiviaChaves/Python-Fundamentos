counter = 0
while counter < 100: #enquanto
    if counter == 4: #quando o contador for igual a 4
        break #PARA
    else:
        pass 
    print(counter)
    counter = counter + 1    

###################################

for verificador in "Python":
    if verificador == "h":
        continue #pula uma interação
    print(verificador)    

######### WHILE E FOR FUNTOS #############

for i in range(2,30): #Percorre um range de valores
    j = 2 #atribuição
    counter = 0 #atribuição
    while j < i: #enquanto
        if i % j == 0:
            counter = 1
            j = j + 1
        else:
            j = j + 1
    
    if counter == 0:
        print(str(i) + " é um número primo")
        counter = 0
    else:
        counter = 0