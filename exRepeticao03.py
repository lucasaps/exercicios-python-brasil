while True:
    nome = input('Digite o nome: ')
    if len(nome) > 3:
        break
    print('O nome deve ter mais que 3 caracteres: ')
while True:
    idade = int(input('Digite a idade: '))
    if 0 < idade < 150:
        break
    print('A idade deve ser entre 0 e 150')
while True:
    salario = float(input('Digite o salário: '))
    if salario >= 0:
        break
    print('O salário deve ser maior ou igual a 0')
while True:
    sexo = str(input('Digite o sexo[f/m]'))
    sexo = sexo.lower()
    if sexo == 'f' or sexo == 'm':
        break
    print('Sexo deve ser f ou m')
while True:
    estado_civil = input('Digite o estado civil[c/s/v/d]')
    estado_civil = estado_civil.lower()
    if estado_civil == 'c' or estado_civil == 's' or estado_civil == 'v' or estado_civil == 'd':
        break
    print('Estado civil deve ser c/s/v/d')
