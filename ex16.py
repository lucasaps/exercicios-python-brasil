from math import ceil


def calcula(area):
    """
    Função que faz os cálculos de quantos litros de linta, e quantas lata de tinta o usuário precisará,
    sempre arredondando para cima
    :param area:
    """

    qntd_litros = area / 3
    qntd_latas = ceil(qntd_litros / 18)
    custo = qntd_latas * 80
    print(
        f'Você precisará de {qntd_litros:.2f}L de tintas. Você precisará comprar {qntd_latas} latas de tinta, o que custará R$ {custo:.2f}')


if __name__ == '__main__':
    area = float(input('Informe o tamanho do local a ser pintado (em metros quadrados): '))
    calcula(area)
