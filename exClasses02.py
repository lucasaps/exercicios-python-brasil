# https://wiki.python.org.br/ExerciciosClasses - 02
# Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, lado=0):
        self.lado = lado

    def alterar_lado(self, valor):
        self.lado = valor

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

if __name__ == '__main__':
    quadrado = Quadrado()
    quadrado.alterar_lado(2)
    print(quadrado.retornar_lado())
    print(quadrado.calcular_area())
    quadrado.alterar_lado(5)
    print(quadrado.retornar_lado())
    print(quadrado.calcular_area())