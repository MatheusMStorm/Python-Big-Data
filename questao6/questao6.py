from openpyxl import Workbook

def posicionarLetra(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    
def listarColunas(char_init, char_final):
    colunas = []

    for i in range(ord(char_init), ord(char_final)+1):
        colunas.append(chr(i))
    
    return colunas

def listarLinhas(num_init, num_final):
    linhas = []
    
    for i in range(num_init, num_final+1):
        linhas.append(i)

    return linhas

char_init = input("Coluna inicial: ").upper()
char_final = input("Coluna final: ").upper()
num_init = int(input("Linha inicial: "))
num_final = int(input("Linha final: "))

linhas_planilha = listarLinhas(num_init, num_final)
colunas_planilha = listarColunas(char_init, char_final)

wb = Workbook()
ws = wb.active

for linha in linhas_planilha:
    for coluna in colunas_planilha:
        ws.cell(row=linha, column=posicionarLetra(coluna), value=coluna+str(linha))

ws.title = "Questão 6"
wb.save("questao6/questao6.xlsx")