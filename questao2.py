# Perguntando ao usuário o seu salário por hora e as horas trabalhadas
sal_hora = float(input("Quanto você ganha por hora? "))
num_horas = int(input("Quantas horas você trabalha por mês? "))

# Definindo as porcentagens referentes ao IR, INSS e sindicato
ir = 0.15
inss = 0.1
sind = 0.02

# Calculando salário bruto, quantia do INSS, IR, sindicato e salário líquido
sal_bruto = round(float(sal_hora * num_horas), 2)
parte_ir = round(float(sal_bruto * ir), 2)
parte_inss = round(float(sal_bruto * inss), 2)
parte_sind = round(float(sal_bruto * sind), 2)
sal_liquido = round(float(sal_bruto - (parte_ir + parte_inss + parte_sind)), 2)

# Imprimindo salário bruto, quantia do INSS, sindicato e salário líquido
print('Salário bruto: R$ ' + str(sal_bruto))
print('Quantia do INSS: R$ ' + str(parte_inss))
print('Quantia do sindicato: R$ ' + str(parte_sind))
print('Salário líquido: R$ ' + str(sal_liquido))