# https://wiki.python.org.br/EstruturaDeRepeticao - 4
"""""Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento."""""

ano = 0
popA = 80_000
popB = 200_000
while popA < popB:
    popA = popA * 1.03
    popA = int(popA)
    popB = popB * 1.015
    popB = int(popB)
    ano += 1

print(f'Demorou {ano} anos para a população de A igualar ou ultrapassar a população de B')
print(f'População de A: {popA}')
print(f'População de B: {popB}')
