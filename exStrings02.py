# https://wiki.python.org.br/ExerciciosComStrings - 2
"""Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário
de trás para frente utilizando somente letras maiúsculas."""

nome = input('Digite seu nome: ')
nome = nome.upper()
invertido = nome[::-1]
print(invertido)
