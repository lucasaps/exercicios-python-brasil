# https://wiki.python.org.br/ExerciciosArquivos
"""Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos."""


def verificar(ip: str) -> bool:
    numeros = ip.split('.')
    if len(numeros) != 4:
        return False

    for n in numeros:
        if not (0 < int(n) < 255):
            return False

    return True


ipsValidos = []
ipsInvalidos = []

with open("lista IPs.txt", 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if verificar(ip):
            ipsValidos.append(ip)
        else:
            ipsInvalidos.append(ip)

with open("resultado IPs.txt", 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ipsValidos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')

    for ip in ipsInvalidos:
        arquivo.writelines(f'{ip}\n')
