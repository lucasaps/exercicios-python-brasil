turno = str(input('Digite o turno que você trabalha[m/v/n]: '))
turno = turno.lower()
if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa tarde!')
elif turno == 'n':
    print('Boa noite!')
else:
    print('Valor inválido!')

