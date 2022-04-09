# Exercício 17 lista Python - Estrutura Sequencial https://wiki.python.org.br/EstruturaSequencial
import math

tamanho = float(input('Informe o tamanho em m2 do local a ser pintado: '))
tamanho_com_folga = tamanho * 1.1
litros_tinta = tamanho_com_folga / 6
lata = litros_tinta / 18
galao = litros_tinta / 3.6

print(f'Se você comprar apenas lata(s), para pintar {tamanho_com_folga}m2, você precisará de {litros_tinta}L'
      f' de tinta, ou seja,  {math.ceil(lata)} latas')
print(f'O que custará R${math.ceil(lata) * 80}')

print(f'Se você comprar apenas galão(ões), para pintar {tamanho_com_folga}m2, você precisará de {litros_tinta}L'
      f' de tinta, ou seja, {math.ceil(galao)} galões'
      f' o que custará R${math.ceil(galao) * 25}')
