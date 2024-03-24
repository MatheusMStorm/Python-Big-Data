import math

def calcularMedia(lista):
    return round(sum(lista)/len(lista), 1)

def contarFrequencia(lista):
    frequencia = {}

    for n in lista:
        if n not in frequencia:
            frequencia[n] = lista.count(n)
    
    return max(frequencia, key=frequencia.get)

def calcularMediana(lista):
    lista = sorted(lista)
    metade = int((len(lista)/2) - 1)
    if len(lista) % 2 == 0:
        mediana = (lista[metade] + lista[metade+1])/2
    else:
        mediana = lista[metade]
    
    return mediana

def calcularVariancia(lista):
    sub_x_media = []

    for n in lista:
        sub_x = (n - calcularMedia(lista))**2
        sub_x_media.append(sub_x)
    
    return round(sum(sub_x_media)/len(lista), 2)

def calcularDesPadrao(lista):
    return round(math.sqrt(calcularVariancia(lista)), 2)

def calcularDados(lista):
    media = calcularMedia(lista)
    moda = contarFrequencia(lista)
    mediana = calcularMediana(lista)
    variancia = calcularVariancia(lista)
    des_padrao = calcularDesPadrao(lista)

    return media, moda, mediana, variancia, des_padrao

temperaturas_nove = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5]

stats_nove_dias = list(calcularDados(temperaturas_nove))

temperaturas_dez = temperaturas_nove
temperaturas_dez.append(20.2)

stats_dez_dias = list(calcularDados(temperaturas_dez))

print(stats_nove_dias)
print(stats_dez_dias)

for t in range(0, len(stats_nove_dias)):
    if stats_nove_dias[t] > stats_dez_dias[t]:
        print(str(stats_nove_dias[t]) + " > " + str(stats_dez_dias[t]))
    elif stats_nove_dias[t] == stats_dez_dias[t]:
        print(str(stats_nove_dias[t]) + " = " + str(stats_dez_dias[t]))
    else:
        print(str(stats_nove_dias[t]) + " < " + str(stats_dez_dias[t]))