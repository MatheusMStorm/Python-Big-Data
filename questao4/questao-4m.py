palavra_a_substituir = input('Digite a palavra que deseja substituir: ')
palavra_a_inserir = input('Digite a palavra que vai ser colocada: ')

with open('questao-4/2024.1_lista_analise_de_dados_Q3.txt', 'r') as fd:
    arquivo = fd.read()
    ocorrencias = arquivo.count(palavra_a_substituir)
    arquivo = arquivo.replace(palavra_a_substituir, palavra_a_inserir)

new_file_name = 'questao-4/' + palavra_a_substituir + '_' + palavra_a_inserir + '_05_03_2024_' + str(ocorrencias) + '.txt'
with open(new_file_name, 'a') as fd:
    fd.write(arquivo)