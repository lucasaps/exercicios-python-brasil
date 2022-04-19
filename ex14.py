LIMITE_QUILOS = 50

def calcula_excesso(peso):
    excesso = peso - LIMITE_QUILOS
    if excesso > 0:
        print(f'O excesso foi de {excesso} kg')
        multa = excesso * 4
        print(f'Deve pagar uma multa de R$ {multa}')
    else:
        print('Não excedeu o limite de peso pescado, logo não paga nenhuma multa')
 


if __name__ == '__main__':
    peso = float(input('Digite o peso do pescado do dia: '))
    calcula_excesso(peso)