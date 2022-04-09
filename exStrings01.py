# https://wiki.python.org.br/ExerciciosComStrings - 1
""""" Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo."""""

stringUm = input('Digite a primeira string: ')
stringDois = input('Digite a segunda string: ')

print(f'String 1: {stringUm}')
print(f'String 2: {stringDois}')

print(f'Tamanho de {stringUm}: {len(stringUm)} caracteres')
print(f'Tamanho de {stringDois}: {len(stringDois)} caracteres')

if len(stringUm) == len(stringDois):
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')

if stringUm == stringDois:
    print('As duas strings possuem o mesmo conteúdo.')
else:
    print('As duas strings possuem conteúdo diferente.')
