#Usando estrutura de decisão:

letra = str(input('Digite uma letra: '))
letra = letra.lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('É vogal')
else:
    print('É consoante')