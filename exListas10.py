vetor_um = []
for i in range(10):
    n = input(f'Digite o valor {i+1}: ')
    vetor_um.append(n)
vetor_dois = []
for i in range(10):
    n = input(f'Digite o valor {i+1}: ')
    vetor_dois.append(n)

vetor_tres = []
for i in range(10):
    vetor_tres.append(vetor_um[i])
    vetor_tres.append(vetor_dois[i])

print(vetor_tres)

