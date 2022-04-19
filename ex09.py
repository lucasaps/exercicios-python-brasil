def converte_temperatura(temp_f):
    temp_convertida = 5 * (temp_f - 32) / 9
    print(f'Temperatura em C = {temp_convertida:.1f}')


if __name__ == '__main__':
    temp_f = float(input('Digite a temperatura em Fahrenheit: '))
    converte_temperatura(temp_f)
