#Fazer um programa que leia o compriemnto do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotensusa.

import math
opos = float(input('Digite o valor do cateto oposto '))
adj = float(input('Digite o valor do cateto adjacente '))
hipo = math.hypot(opos, adj)
print(f'O valor da hipotenusa é {hipo:.2f}')