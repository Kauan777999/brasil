#O mesmo professor do desafio anterior quer sortear a ordem e apresentação de trabalho dos alunos. Faça um programa que leia o noome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.shuffle(lista)  #shuffle usado para embaralhar
print('A ordem de apresentação será: ')
print(lista)