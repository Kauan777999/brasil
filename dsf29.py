velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print(f'MULTADO! Você ultrapsssou o limite de velocidade que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pegar um multa de R${multa}')
else:
    print('Está dentro dos limites tenha uma boa viagem')

