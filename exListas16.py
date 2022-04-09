# https://wiki.python.org.br/ExerciciosListas - 16

salarios = [205, 290, 345, 345, 400, 420, 640, 690, 1000, 2030, 3000]
contadorFaixas = [0] * 9

for salario in salarios:
    indice = salario // 100 - 2
    indiceMax = len(contadorFaixas) - 1
    indice = min(indiceMax, indice)
    contadorFaixas[indice] += 1

print(contadorFaixas)
