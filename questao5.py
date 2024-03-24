nome, sexo, est_civil = '', '', ''
idade, salario = 0,0

while len(nome) < 3:
    nome = input('Digite seu nome: \n')

    if len(nome) < 3:
        print('Inválido! O nome deve ser maior que 3 caracteres.')

while sexo.upper() != 'F' and sexo.upper() != 'M':
    sexo = input('Informe o sexo (F - Feminino ou M - Masculino): \n')

    if sexo.upper() != 'F' and sexo.upper() != 'M':
        print('Inválido!')

while est_civil.upper() != 'S' and est_civil.upper() != 'C' and est_civil.upper() != 'V' and est_civil.upper() and 'D':
    est_civil = input('Estado civil (S - Solteiro, C - Casado, V - Viúvo, D - Divorciado): \n')

    if est_civil.upper() != 'S' and est_civil.upper() != 'C' and est_civil.upper() != 'V' and est_civil.upper() and 'D':
        print('Inválido!')

while idade < 0 and idade > 150:
    idade = input ('Digite sua idade: \n')

    if idade < 0 and idade > 150:
        print('Inválido! Digite uma idade entre 0 e 150.')

while salario <= 0:
    salario = input('Quanto ganha por mês? \n')

    if salario <= 0:
        print('Inválido! Digite um salário maior que zero.')