def calcula(inteiro_um, inteiro_dois, real):
    operacao_um = (2 * inteiro_um) * (inteiro_dois/2)
    operacao_dois = (3 * inteiro_um) + real
    operacao_tres = real ** 3
    print(f'Operação um: {operacao_um}')
    print(f'Operação dois: {operacao_dois}')
    print(f'Operação três: {operacao_tres}')


if __name__ == '__main__':
    inteiro_um = int(input('Digite o primeiro inteiro: '))
    inteiro_dois = int(input('Digite o segundo inteiro: '))
    real = float(input('Digite o número real: '))
    calcula(inteiro_um, inteiro_dois, real)