while True:
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    if senha == nome:
        print('A senha não pode ser igual ao nome de usuário')
    else:
        break

#print(f'usuário: {nome}')
#print(f'senha: {senha}')
print('Fim do programa')