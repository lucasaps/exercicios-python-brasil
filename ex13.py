def peso_ideal(altura):
    altura = altura / 100
    peso_homem = 72.7 * altura - 58
    peso_mulher = 62.1 * altura - 44.7
    print(f'Peso ideal para homem: {peso_homem:.2f} kg')
    print(f'Peso ideal para mulher: {peso_mulher:.2f} kg')


if __name__ == '__main__':
    altura = int(input('Digite a altura em cm: '))
    peso_ideal(altura)
