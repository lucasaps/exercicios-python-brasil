def calcula_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


if __name__ == '__main__':
    nota_um = float(input('Digite a primeira nota: '))
    nota_dois = float(input('Digite a segunda nota: '))
    nota_tres = float(input('Digite a terceira nota: '))
    nota_quatro = float(input('Digite a quarta nota: '))
    print(calcula_media(nota_um, nota_dois, nota_tres, nota_quatro))
