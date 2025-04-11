#Questão 1

resultado = 2 + (3 * 4) - 5
print(f'Qual o valor da empressão? ', resultado)

#Questão 2

resultado = 2 + 3 * (4 - 5)
print(f'Qual o valor da expressão? ', resultado)

#Questão 3

resultado = 12 * 2 % 10
print(f'Qual o valor da expressão? ', resultado)

#Questão 4

resultado = 4 * 3 **2 // 10
print(f'Qual o valor da expressão? ', resultado)

#Questão 5

resultado = 2 ** 3 ** 2
print(f'Qual o valor da expressão? ', resultado)

#Questão 6

resultado = (-2)**4
print(F'Qual o resultado da expressão? ', resultado)

#Questão 7

nota = float(input('Digite a nota: '))
resultado = 3 < nota < 5
print(resultado)

#Questão 8

ano = int(input("Digite um ano: "))
print((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))

#Questão 9

soma = 0
soma = 0
num = int(input())

while num != 0:
    soma += num
    num = int(input())

print(soma)


#Questão 10

n = int(input())
k = int(input())
print(n ** k)

#Questão 11

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input())
print(fatorial(n))

#Questão 12

n = int(input())
i = int(input())
j = int(input())

multiplos = []
num = 0

while len(multiplos) < n:
    if num % i == 0 or num % j == 0:
        multiplos.append(num)
    num += 1
print(*multiplos)

#Questão 13

def mdc(a, b):                      # Define uma função chamada 'mdc' que recebe dois inteiros 'a' e 'b'.
    while b != 0:                   # Enquanto 'b' for diferente de zero...
        a, b = b, a % b             # Atualiza 'a' com o valor de 'b' e 'b' com o resto da divisão de 'a' por 'b'.
    return a                        # Quando 'b' for zero, 'a' é o MDC. Retorna esse valor.

#Questão 14

n = int(input("Quantidade de números: "))   # Lê um número inteiro e armazena em 'n'. Esse será o tamanho da sequência.
soma = 0                                    # Começamos com a soma igual a zero.

for _ in range(n):                          # Executa o bloco abaixo 'n' vezes (para cada número da sequência).
    x = int(input("Digite um número: "))    # Lê um número inteiro da sequência.
    if x % 2 == 0:                          # Verifica se o número é par (se o resto da divisão por 2 é 0).
        soma += x                           # Se for par, adiciona esse número à soma.

print("Soma dos pares:", soma)             # Exibe a soma dos números pares.

#Questão 15

n = int(input("Quantidade de números: "))    # Lê o número total de elementos da sequência.
pares = 0                                    # Inicializa a contagem de pares.
impares = 0                                  # Inicializa a contagem de ímpares.

for _ in range(n):                           # Laço que se repete 'n' vezes.
    x = int(input("Digite um número: "))     # Lê um número da sequência.
    if x % 2 == 0:                           # Se for par...
        pares += 1                           # Incrementa a contagem de pares.
    else:                                    # Senão...
        impares += 1                         # Incrementa a contagem de ímpares.

print("Pares:", pares)                       # Mostra quantos pares foram contados.
print("Ímpares:", impares)                   # Mostra quantos ímpares foram contados.

#Questão 16


n = input("n: ").lstrip("0")
d = input("d: ")
print(f"O dígito {d} ocorre {n.count(d)} vezes em {n}")

#Questão 17

n = int(input("Digite um número inteiro n > 1: "))
divisor = 2

while n > 1:
    multiplicidade = 0
    while n % divisor == 0:
        n //= divisor
        multiplicidade += 1
    if multiplicidade > 0:
        print(f"fator {divisor} multiplicidade {multiplicidade}")
    divisor += 1

#Questão 18

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Digite a quantidade de números: "))
sequencia = []

for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    sequencia.append(num)

resultado = sequencia[0]
for num in sequencia[1:]:
    resultado = mdc(resultado, num)

print(f"O máximo divisor comum é {resultado}")

#Questão 20

def eh_primo(n):                                  # Função que verifica se um número é primo
    if n < 2: return False                         # Números < 2 não são primos
    for i in range(2, int(n**0.5)+1):              # Testa divisores de 2 até a raiz quadrada de n
        if n % i == 0: return False                # Se for divisível, não é primo
    return True                                    # Se passar ileso, é primo

primos = 0                                         # Contador de números primos
while True:
    x = int(input())                               # Lê um número
    if x == 0: break                               # Se for zero, para
    if eh_primo(x): primos += 1                    # Se for primo, aumenta o contador

print("Quantidade de primos:", primos)             # Exibe o total de primos encontrados


    
