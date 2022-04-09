# https://wiki.python.org.br/EstruturaDeRepeticao - 7
# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
media = 0.0
contador = 0

while contador < 5:
    contador += 1
    num = float(input('Digite um número: '))
    soma = soma + num
    media = soma / contador
    print(f'Soma é {soma} e a média é {media}')
