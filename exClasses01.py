# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.material = material
        self.cor = cor
        self.circunferencia = circunferencia

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(f'Cor da bola: {self.cor}')


if __name__ == '__main__':
    bola = Bola('branca', 5, 'couro')
    bola.mostraCor()
    bola.trocaCor('azul')
    bola.mostraCor()
