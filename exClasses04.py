# https://wiki.python.org.br/ExerciciosClasses - 04
# Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
"""Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, cm):
        self.altura += cm


if __name__ == '__main__':
    pessoa = Pessoa('Fulano', 2, 12, 80)
    for _ in range(22):
        pessoa.envelhecer()
        print(f'Idade de {pessoa.nome} é {pessoa.idade}. Altura é: {pessoa.altura} cm')
