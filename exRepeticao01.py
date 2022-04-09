# https://wiki.python.org.br/EstruturaDeRepeticao
"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido."""

while True:
    try:
        nota = float(input('Digite uma nota entre 0 e 10: '))
    except ValueError:
        print('Erro. Deve ser fornecido uma nota entre 0 e 10: ')
    else:
        if 0 <= nota <= 10:
            print(f'Nota: {nota}')
            break
        else:
            print('Erro. Deve ser fornecida uma nota entre 0 e 10: ')
