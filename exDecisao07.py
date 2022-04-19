#Usando estrutura de decisão. Há maneiras mais fáceis

num_um = int(input('Digite o primeiro número: '))
num_dois = int(input('Digite o segundo número: '))
num_tres = int(input('Digite o terceiro número: '))

if num_um > num_dois:
    if num_um > num_tres:
        print(f'O maior é {num_um}')
        if num_dois > num_tres:
            print(f'O menor é {num_tres}')
        else:
            print(f'O menor é {num_dois}')
    else:
        print(f'O maior é {num_tres}')
        print(f'O menor é {num_um}')

else:
    if num_dois > num_tres:
        print(f'O maior é {num_dois}')
        if num_um > num_tres:
            print(f'O menor é {num_tres}')
    else:
        print(f'O maior é {num_tres}')
        if num_um < num_tres:
            print(f'O menor é {num_um}')

