import json

f = open('data.json')

data = json.load(f)

diccionario = dict()

lista = []

for x in range(len(data)):
    llaves = diccionario.keys()
    if data[x]['name'] not in llaves:
        diccionario[data[x]['name']] = [[data[x]['data'],data[x]['semana']]]
    else:
        diccionario[data[x]['name']].append([data[x]['data'],data[x]['semana']])

for x in range(len(diccionario)):
    dict_temp = {}
    key_temp = list(diccionario.keys())[x]
    lista_ordenada = []
    for y in range(len(diccionario[key_temp])):
        lista_ordenada.append(diccionario[key_temp][y][0])
    dict_temp[key_temp] = lista_ordenada
    lista.append(dict_temp)
print(lista)

print(diccionario)