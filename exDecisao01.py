num_um = float(input('Digite o primeiro número: '))
num_dois = float(input('Digite o segundo número: '))

if num_um > num_dois:
    print(f'O maior número é {num_um}')
elif num_dois > num_um:
    print(f'O maior número é {num_dois}')
else:
    print(f'São iguais')