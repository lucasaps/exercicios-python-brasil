def calcula_salario_mes(salario_por_hora, horas_mes):
    salario = salario_por_hora * horas_mes
    print(f'Salário por mês = R$ {salario}')
    


if __name__ == '__main__':
    salario_por_hora = float(input('Digite o salário por hora: '))
    horas_mes = float(input('Digite a quantidade de horas trabalhadas por mês: '))
    calcula_salario_mes(salario_por_hora, horas_mes)