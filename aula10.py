#Condições - Simples e compostas

#A grande maioria dos programas possuem condições

#if = "se"   else = "Senão"  importante!

#Primeira representação de estrutura condicional

#Exemplo

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('carro velho')

#Todo comando que estiver colado do lado esquerdo da tela vai ser executado sempre, mas todo comando que tiver com idetenção para dentro ele pode ser executado ou não, vai depender da situação
#Mas nesse caso ou ele vai escrever carro novo ou carro ou carro velho

#Exemplo, exercicio

nome = str(input('Qual é seu nome? '))
if nome == 'Kauan':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é normal!')
print(f'Bom dia {nome}!')

#Exemplo, exercicio

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media}')
if media <= 6:
    print('Sua nota foi baixa')
else:
    print('Sua nota foi alta')
