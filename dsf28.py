from random import randint      #randint: Determinar um limite para o computador escolher
computador = randint(0 , 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
if jogador == computador:
    print('Prabéns você conseguiu me vencer')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')