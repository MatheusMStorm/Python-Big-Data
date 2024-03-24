with open("2024.1_lista_analise_de_dados_Q3.txt", "r", encoding="utf-8") as texto:
    conteudo = texto.readlines()

caracteres = ',.'
frase = conteudo[1].rstrip('\n')

for i in range(0, len(caracteres)):
    frase = frase.replace(caracteres[i], '')

palavras = frase.split(' ')
palavras_repetidas = []
repeticoes_palavra = []

for palavra in palavras:
    if palavra not in palavras_repetidas:
        repeticoes_palavra.append(palavras.count(palavra))
        palavras_repetidas.append(palavra)

dicionario_palavras = {}

for i in range(0, len(palavras_repetidas)):
    novo = {palavras_repetidas[i]: repeticoes_palavra[i]}
    dicionario_palavras.update(novo)

print(dicionario_palavras)