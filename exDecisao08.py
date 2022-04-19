#Usando estrutura de decisão. Há maneiras mais fáceis

preco_um = float(input('Digite o primeiro preço: '))
preco_dois = float(input('Digite o segundo preço: '))
preco_tres = float(input('Digite o terceiro preço: '))

if preco_um < preco_dois:
    if preco_um < preco_tres:
        print(f'O menor é {preco_um}. Compre')
    else:
        print(f'O menor é {preco_tres}. Compre')
else:
    if preco_dois < preco_tres:
        print(f'O menor é {preco_dois}. Compre')
    else:
        print(f'O menor é {preco_tres}. Compre')

