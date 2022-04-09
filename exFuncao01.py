# https://wiki.python.org.br/ExerciciosFuncoes - 1

def minhaFuncao(num: int):
    for i in range(1, num + 1):
        for _ in range(i):
            print(i, end='   ')
        print('')


minhaFuncao(5)
