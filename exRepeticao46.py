saltos = []
while True:
    nome = str(input('Digite o nome do atleta: '))
    if nome == '':
        break
    for i in range(5):
        salto = float(input(f'Digite a distância do salto {i + 1}: '))
        saltos.append(salto)
    print()
    print(f'Atleta: {nome}')
    print(f'Primeiro salto: {saltos[0]} m')
    print(f'Segundo salto: {saltos[1]} m')
    print(f'Terceiro salto: {saltos[2]} m')
    print(f'Quarto salto: {saltos[3]} m')
    print(f'Quinto salto: {saltos[4]} m')
    saltos.sort()
    media = (saltos[1] + saltos[2] + saltos[3]) / 3
    print()
    print(f'Melhor salto: {saltos[4]} m')
    print(f'Pior salto: {saltos[0]} m')
    print(f'Média dos demais salto: {media:.2f} m')
    print()
    print('Resultado final: ')
    print(f'{nome}: {media:.2f} m')
    saltos.clear()

