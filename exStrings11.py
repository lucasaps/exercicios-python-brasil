# https://wiki.python.org.br/ExerciciosComStrings - 11
"""Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto
e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado."""
import random

# Método para abrir um arquivo no modo somente leitura e pegar todas as palavras
with open("palavras.txt", "r") as file:
    textoTodo = file.read()
    palavras = list(map(str, textoTodo.split('\n')))

palavraEscolhida = random.choice(palavras).upper()  # Pega uma palavra aleatória do arquivo palavras.txt
numLetras = len(palavraEscolhida)
exibeTraços = '_' * numLetras

contadorErros = 0
contadorAcertos = 0

while contadorErros < 7:
    posicoesEncontradas = []  # Para guardar as posições em que a letra digitada estão na palavra
    letraDigitada = input('Digite uma letra: ').upper()
    checa = palavraEscolhida.find(letraDigitada)  # Procura a primeira posição em que a letra digitada está na palavra
    posicoesEncontradas.append(checa)  # Guarda o índice da letra encontrada ou -1 se não encontrar
    if checa == -1:  # Se não encontra a letra
        contadorErros += 1
        print(f'Você errou pela {contadorErros}ª vez. Tente de novo')
    else:  # Se encontra a letra
        # Procura se tem mais ocorrências da letra começando do índice já encontrado
        while checa != -1:
            checa = palavraEscolhida.find(letraDigitada, checa + 1)
            posicoesEncontradas.append(checa)  # Guarda os índices correspondentes às letras encontradas
            contadorAcertos += 1

        posicoesEncontradas.remove(-1)  # Remove o -1 que foi adicionado quando não encontrou a letra
        # print(posicoesEncontradas)
        for i in posicoesEncontradas:  # Troca os traços pelas letras encontradas
            exibeTraços = exibeTraços[:i] + letraDigitada + exibeTraços[i + 1:]
            if contadorAcertos == len(palavraEscolhida):
                print("Parabéns! Acertou a palavra!")
                exit()
        print('A palavra é: ' + exibeTraços)
print("Enforcado!")
print(f'A palavra era: {palavraEscolhida}')
