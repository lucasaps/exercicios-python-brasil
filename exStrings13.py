import random


def embaralha(string):
    random.shuffle(string)
    palavra_embaralhada = ''.join(string)
    return palavra_embaralhada


if __name__ == '__main__':
    # abre um arquivo no modo somente leitura e pegar todas as palavras
    with open("palavras.txt", "r") as file:
        textoTodo = file.read()
        palavras = list(map(str, textoTodo.split('\n')))

    palavraEscolhida = random.choice(palavras).upper()  # Pega uma palavra aleatória do arquivo palavras.txt
    palavra = []
    for _ in palavraEscolhida:
        palavra.append(_)
    print(embaralha(palavra))
    contador = 0
    while contador < 6:
        tentativa = str(input('Qual a palavra?').upper())
        if tentativa == palavraEscolhida:
            print('Parabéns, você acertou!')
            exit()
        else:
            print('Essa não é a palavra!')
            contador += 1
    print(f'A palavra era: {palavraEscolhida}')
