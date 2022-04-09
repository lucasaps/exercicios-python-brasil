# https://wiki.python.org.br/ExerciciosListas - 15
notas = []
while True:
    nota = float(input('Digite uma nota ou -1 para encerrar: '))
    if (nota == -1.0):
        break
    else:
        notas.append(nota)

if len(notas) == 0:
    print('Fim do programa!')
    exit()

print(f'Foram lidas {len(notas)} notas')
print(' '.join([str(n) for n in notas]))

tamanho = len(notas)

print('Valores na ordem inversa na vertical:')
while tamanho - 1 >= 0:
    print(notas[tamanho - 1])
    tamanho -= 1

print(f'Soma das notas: {sum(notas)}')
media = (sum(notas)) / len(notas)
print(f'A média das notas: {media}')

tamanho = len(notas)



print('Notas acima da média: ')
print(' '.join([str(n) for n in notas if n > media]))

menores = []
for i in range(tamanho):
    if notas[i] < 7.0:
        menores.append(notas[i])

print(f'Existem {len(menores)} valor(es) menor(es) que 7. São eles: ')
print(menores)
print("Fim do programa!")
