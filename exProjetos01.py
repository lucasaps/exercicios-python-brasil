# https://wiki.python.org.br/ListaDeExerciciosProjetos - 01. Dois primeiros itens

def transformar_em_mb(tamanho_em_bytes: str) -> float:
    return int(tamanho_em_bytes) / (2 ** 10) ** 2


lista_de_dados = []
cabecalho = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso"""

with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_mb(linha[16:])
        lista_de_dados.append((tamanho_em_disco, usuario))

cabecalho = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
"""

n = int(input('Digite a quantidade de linhas a seres exibidas: '))

lista_de_dados.sort(reverse=True)
lista_de_dados = lista_de_dados[:n]

with open('relatorio.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for tamanho, _ in lista_de_dados])
    media = tamanho_total_consumido / len(lista_de_dados)
    arquivo.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados):
        tamanho_em_disco, usuario = dados
        arquivo.writelines(f'{(indice + 1):<4}    {usuario}       {tamanho_em_disco:9.2f} MB'
                           f'             {tamanho_em_disco / tamanho_total_consumido:>6.2%}\n')
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')
