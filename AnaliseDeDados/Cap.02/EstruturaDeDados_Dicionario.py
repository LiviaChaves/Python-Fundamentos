#Lista
estudantes_list = ["Aluno1",26,"Aluno2",27,"Aluno3",25]
print(estudantes_list)

#DICIONÁRIO
estudantes_dic = {"Aluno1": 26, "Aluno2": 27, "Aluno3": 25}
print(estudantes_dic)

print(estudantes_dic["Aluno2"]) # funciona como uma "chave" vai retornar o 27 
print(estudantes_dic["Aluno3"]) 
print(estudantes_dic["Aluno1"])
estudantes_dic["Aluno4"] = 28 # adicona na lista
print(estudantes_dic)

estudantes_dic.clear() #Limpa a lista (deixa vazia)
del estudantes_dic #deleta o dicionario
#print(estudantes_dic)

estudantes = {'Cristiano':25 , 'Fernanda': 28,'Mateus':22,'Tamires':23}
print(estudantes)
print(len(estudantes))

print(estudantes.keys()) # só imprime as chaves
print(estudantes.values()) #só imprime os valores
print(estudantes.items()) #imprime o dicionario (tudo)


estudantes2 = {'Maria':26,'João':23,'Joana':27}
print(estudantes2)

estudantes.update(estudantes2) #atualiza os componentes de estudantes com os elementos de estudantes2
print(estudantes)

dis = {} # vazio
dis['Livia'] = 21 #adiciona elemento a lista vazia dis
print(dis)
dis[10] = 11
print(dis)

dis2 = {}
dis2['teste'] = 10
dis2['key'] = 'teste' # Chave e valor podem ter valores iguais, mas representam coisas diferentes
print(dis2)
dis2['key2'] = 10
dis2['key3'] = 5.6
print(dis2)

a = dis2['key'] # associando a uma variavel
b = dis2['key2'] # associando a uma variavel
c = dis2['key3'] # associando a uma variavel
print(a,b,c)


dis3 = {'key1':1890,'key2':[22,365,73.4],'key3':['leite','maça','batata']} # Dicionário de listas
print(dis3)

print(dis3['key2']) # imprime os valores referentes a essa chave
print(dis3['key3']) # imprime os valores referentes a essa chave
print(dis3['key1']) # imprime os valores referentes a essa chave

print(dis3['key3'][0].upper()) #acessa/imprime o item da lista , dentro do dicionario

var1 = dis3['key2'][0] - 10 # operação com um iten da lista que esta dentro do dicionario
print(var1)

#CRIANDO DICIONÁRIOS ANINHADOS

dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])
