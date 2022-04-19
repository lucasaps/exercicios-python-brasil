def calcula_area_quadrado_imprime_dobro(lado):
    print((lado * lado) * 2)


if __name__ == '__main__':
    lado = float(input('Digite o lado do quadrado: '))
    calcula_area_quadrado_imprime_dobro(lado)
