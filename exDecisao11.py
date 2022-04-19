def imprime_dados(salario, salario_anterior, percentual):
    print(f'Salário anterior: {salario_anterior}')
    print(f'Percentual de aumento: {percentual}')
    print(f'Aumento salarial: {salario - salario_anterior:.2f}')
    print(f'Novo salário: {salario:.2f}')


def calcula_reajuste(salario):
    if salario_anterior <= 288:
        salario = salario_anterior * 1.2
        percentual = '20%'
        imprime_dados(salario, salario_anterior, percentual)
    elif 288 < salario_anterior <= 700:
        salario = salario_anterior * 1.15
        percentual = '15%'
        imprime_dados(salario, salario_anterior, percentual)
    elif 700 < salario_anterior <= 1500:
        salario = salario_anterior * 1.1
        percentual = '10%'
        imprime_dados(salario, salario_anterior, percentual)
    else:
        salario = salario_anterior * 1.05
        percentual = '5%'
        imprime_dados(salario, salario_anterior, percentual)


salario_anterior = float(input('Digite o valor do salário antes do aumento: '))
calcula_reajuste(salario_anterior)
