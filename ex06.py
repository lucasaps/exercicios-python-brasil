import math


def calcula_area_circulo(raio):
    area = math.pi * (raio * raio)
    print(f'Área do círculo: {area:.2f}')


if __name__ == '__main__':
    raio = float(input('Digite o valor do raio do círculo: '))
    calcula_area_circulo(raio)
