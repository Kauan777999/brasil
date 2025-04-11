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

#Questão 6

def matriz_maior(A, m, n):
    # { vetor contendo o maior elemento de cada linha }
    for i in range(m):  # para i ← 1 até m faça (em Python é de 0 até m-1)
        Maior = A[i][0]  # Maior(i) ← A(i, 1)

        for j in range(1, n):  # para j ← 2 até n faça (começa do índice 1)
            if A[i][j] > Maior:  # se A(i,j) > Maior(i) então
                Maior = A[i][j]  # Maior(i) ← A(i,j)
        
        print(f"{i}: {Maior}")  # escreva i, Maior(i)

#Questão 7

def calcular_pi(n):
    pi = 0
    for k in range(n):
        pi += (-1)**k / (2*k + 1)
    return 4 * pi

valores_n = [10, 100, 1000, 10000]

for n in valores_n:
    print(n, calcular_pi(n))

#Questão 8

def raiz_babilonica(a):
    x = a  
    while abs(x - a / x) > 1e-6:
        x = (x + a / x) / 2
    return x  

valores_a = [2, 10, 25, 50]

for a in valores_a:
    print(a, raiz_babilonica(a))




