##https://wiki.python.org.br/EstruturaDeDecisao Ex 19
"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão
as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina."""

valorSaque = 59
numNotas100 = valorSaque // 100
numNotas50 = 0
numNotas10 = 0
numNotas5 = 0
numNotas1 = 0
resto = valorSaque % 100

while (resto > 0):
    if resto > 0:
        if resto >= 50:
            numNotas50 += 1
            resto = resto - 50
        else:
            if resto >= 10:
                numNotas10 += 1
                resto = resto - 10
            elif 10 > resto >= 5:
                numNotas5 += 1
                resto = resto - 5
            else:
                numNotas1 = numNotas1 + resto
                resto = resto - numNotas1

print(f'{numNotas100}  notas de 100, {numNotas50} notas de 50, {numNotas10} notas de 10, {numNotas5} notas de 5,'
      f' {numNotas1} notas  de 1')
