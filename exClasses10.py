# https://wiki.python.org.br/ExerciciosClasses - 10

class bombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, dinheiro):
        litros = dinheiro / self.valor_litro
        self._verificar_abastecimento(litros, dinheiro)

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        self._verificar_abastecimento(litros, valor)

    def _verificar_abastecimento(self, litros, dinheiro):
        if litros > self.quantidade_combustivel:
            print(f'Quantidade de combusítvel insuficiente na bomba. Restam apenas {self.quantidade_combustivel:.2f}L')
            print(f'Faltam {litros - self.quantidade_combustivel:.2f}L para atender seu pedido')
        else:
            self.quantidade_combustivel -= litros
            print(f'Foram abastecidos {litros:.2f}L a um valor de R$ {litros * self.valor_litro:.2f}')
            print(f'Resta na bomba {self.quantidade_combustivel:.2f}L de combustível')

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        return self.valor_litro

    def alterar_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo

    def alterar_quantidade(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        return self.quantidade_combustivel


if __name__ == '__main__':
    bomba = bombaCombustivel('Álcool', 4.59, 100)
    bomba.abastecer_por_valor(100)
    bomba.abastecer_por_litro(50)
    bomba.alterar_valor(5.59)
    bomba.abastecer_por_litro(50)
    bomba.alterar_quantidade(112)
    bomba.abastecer_por_litro(50)
    bomba.abastecer_por_valor(410)
