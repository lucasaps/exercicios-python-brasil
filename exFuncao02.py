# https://wiki.python.org.br/ExerciciosFuncoes - 2

def minhaFuncao(num: int):
    for i in range(1, num + 1):
        for num in range(i):
            print(num + 1, end=' ')
        print(' ')


minhaFuncao(5)
