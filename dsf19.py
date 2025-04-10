#Um professor quer sortear um dos seus quatro alunos para apagar o qaudro. Faça um programa que ajude ele. Lendo o nome deles e escrevendo o nome escolhido
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]   #Criou uma lista. sempre fica entre []
escolhido = random.choice(lista)  #metódo choice usado para fazer escolhas
print(f'O aluno esolhido foi {escolhido}')