# https://wiki.python.org.br/EstruturaDeRepeticao - 7
# Faça um programa que leia 5 números e informe o maior número.

maior = -1

for _ in range(5):
    num = int(input('Digite um número: '))
    if num >= maior:
        maior = num

print(f'O maior número digitado foi {maior}')
