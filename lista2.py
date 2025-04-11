#Nome: José Victor Kauã Silva Rodrigues
#Matrícula: 20240040901

#Questão 1:
#Objetivo: Converter grau fahrenheit para celsius

c = float(input('Informe a temperatura em °F: '))
f = (9 * c/ 5) + 32    #Fazer conversão das temperaturas por meio dessa fórmula
print(f'A temperatura de {f}°F corresponde {c}°C')

#Questão 3:
#Objetivo: Determinar a precisão a máquina

def calcular_epsilon():
    epsilon = 1.0
    while True:
        if 1.0 + epsilon == 1.0:
            break
        epsilon = epsilon / 2
    print('Precisão da máquina (Epsilon): ', epsilon * 2)
calcular_epsilon()

#Questão 4:
#Obejivo: Verificaar propriedades dos números ímpares

n = int(input('Digite o valor de n: '))
soma = 0
for i in range(1, 2 * n, 2):
    soma = soma + 1

print('Soma dos', n,'primeiros ímpares: ', soma)
print("n² =", n ** 2)

#Questão 5
#Objetivo: Calcular média aritmétrica e desvio padrão
import math
def media_desvio(n, x):
    n = len(n, x)
    soma = 0
    soma2 = 0
    for i in range(n):
        soma += x[i]
        soma2 += x[i]**2
    media = soma / n
    desvio_padrao = math.sqrt((soma2 - (soma ** 2) / n) / (n - 1))

    return media, desvio_padrao
