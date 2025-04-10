#Desenvolva um programa que pergunta a distância de uma viagem em km. Calcula o preço da passagem. Cobrando R$0.50 por km para viagens de até 200 km a R$0.45 para viagens mais longas.

distância = float(input('Qual é a distânciaa de sua viagem'))
print(f'Você está prestes a começar uma viagem de {distância}km')
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distâncis = 0.45
print(f'É o preço da sua passagem será de R${preço}')