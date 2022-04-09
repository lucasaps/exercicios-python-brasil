# https://wiki.python.org.br/ExerciciosListas - 2
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for _ in range(10):
    num = float(input('Digite um número real: '))
    numeros.append(num)
    print(numeros)

numeros.reverse()
print(f'Vetor invertido: {numeros}')
