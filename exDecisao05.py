# Exercício 5 da lista https://wiki.python.org.br/EstruturaDeDecisao
# Recebe duas notas e imprime aprovodado se media=7, reprovado se media<7 ou aprovado
# com distinção se média=10

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media < 7:
    print(f'REPROVADO! A média do aluno foi {media:.2f}')
elif media >= 7 and media < 10:
    print(f'APROVADO! A média do aluno foi {media:.2f}')
else:
    print(f'APROVADO COM DISTINÇÃO! A média foi: {media:.2f}')
