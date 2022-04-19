# Recebe 'm' ou'f' e imprime masculino, feminino ou inválido
sexo = input('Digite o sexo(m/f): ')
sexo = sexo.lower()
if sexo == 'm':
    print("Masculino")
elif sexo == 'f':
    print('Feminino')
else:
    print('Inválido')
