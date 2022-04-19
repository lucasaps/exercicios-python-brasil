def converte_temperatura(temp_c):
	temp_convertida = temp_c * 1.8 + 32
	print(f'Temperatura em C = {temp_convertida:.1f}F')
    
    
if __name__ == '__main__':
    temp_c = float(input('Digite a temperatura em Celsius: '))
    converte_temperatura(temp_c)