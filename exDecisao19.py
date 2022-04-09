# https://wiki.python.org.br/EstruturaDeDecisao Ex 19
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros'''

num = int(input('Digite um número menor que 1000: '))
centenas_str = dezenas_str = unidade_str = ''

partesNumerica = 0

centenas_int, num = divmod(num, 100)

if centenas_int == 1:
    centenas_str = "1 centena"
    partesNumerica += 1
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'
    partesNumerica += 1

dezenas_int, num = divmod(num, 10)

if dezenas_int == 1:
    dezenas_str = "1 dezena"
    partesNumerica += 1
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'
    partesNumerica += 1

if num == 1:
    unidade_str = "1 unidade"
    partesNumerica += 1
elif num > 1:
    unidade_str = f'{num} unidades'
    partesNumerica += 1

if partesNumerica == 0:
    print('O número 0 não possui centenas, dezenas ou unidades')
elif partesNumerica == 1:
    print(centenas_str + dezenas_str + unidade_str + '.')
elif partesNumerica == 3:
    print(centenas_str + ', ' + dezenas_str + ' e ' + unidade_str + '.')
elif partesNumerica == 2:
    if centenas_str != '':
        segundaParte = dezenas_str + unidade_str + '.'
        print(f'{centenas_str}' + ' e ' + segundaParte)
    else:
        print(dezenas_str + ' e ' + unidade_str + '.')
