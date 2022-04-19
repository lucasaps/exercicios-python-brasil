def peso_ideal(altura):
    altura = altura / 100
    peso = 72.7 * altura - 58
    print(f'Peso ideal: {peso:.2f} kg')


if __name__ == '__main__':
    altura = int(input('Digite a altura em cm: '))
    peso_ideal(altura)
