# https://wiki.python.org.br/ExerciciosListas - 1
# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for _ in range(5):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)

    print(lista)
