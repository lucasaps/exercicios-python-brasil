def calcula_salario_mes(salario_por_hora, horas_mes):
    salario = salario_por_hora * horas_mes
    pagou_ir = (salario * 11) / 100
    pagou_inss = (salario * 8) / 100
    pagou_sindicato = (salario * 5) / 100
    salario_liquido = salario - pagou_ir - pagou_inss - pagou_sindicato
    print(f'Salário bruto = R$ {salario:.2f}')
    print(f'IR (11%) : R$ {pagou_ir:.2f}')
    print(f'INSS (8%) : R$ {pagou_inss:.2f}')
    print(f'Sindicato (5%) : R$ {pagou_sindicato:.2f}')
    print(f'Salário Líquido : R$ {salario_liquido:.2f}')


if __name__ == '__main__':
    salario_por_hora = float(input('Digite o salário por hora: '))
    horas_mes = float(input('Digite a quantidade de horas trabalhadas por mês: '))
    calcula_salario_mes(salario_por_hora, horas_mes)
