#Usando estrutura de repetição. Há maneiras melhores

resposta_um = input('Telefonou para a vítima?')
resposta_dois = input("Esteve no local do crime?")
resposta_tres = input("Mora perto da vítima?")
resposta_quatro = input("Devia para a vítima?")
resposta_cinco = input("Já trabalhou com a vítima?")

contador = 0

if resposta_um == 's':
    contador += 1
if resposta_dois == 's':
    contador += 1
if resposta_tres == 's':
    contador += 1
if resposta_quatro == 's':
    contador += 1
if resposta_cinco == 's':
    contador += 1

if contador < 2:
    print('Inocente')
elif contador == 2:
    print('Suspeito')
elif 3 <= contador <= 4:
    print('Cúmplice')
else:
    print('Culpado')
