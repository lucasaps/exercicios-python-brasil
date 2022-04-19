def calcula_tempo_download(tamanho, velocidade):
    tempo = tamanho / velocidade / 60
    return tempo


if __name__ == '__main__':
    tamanho_arquivo = float(input('Digite o tamanho do arquivo (em Mb): '))
    velocidade_link = float(input('Digite a velocidade do link (em Mbps: '))
    calcula_tempo_download(tamanho_arquivo, velocidade_link)
    print(f'Tempo de download: {calcula_tempo_download(tamanho_arquivo, velocidade_link):.2f} minutos')
