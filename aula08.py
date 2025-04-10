#Principais coisas a saber
    #math: Significa matemática
    #ceil: Faz o arredondamento do número
    #floor: Faz o arredondamento para baixo
    #trunc: Elimina da virgula pra frente sem fazer arredondamento nenhum
    #pow: Que é potência , que vai ter quase a mesma finalidade que os **
    #sqrt: modúlo usado quando se quer calcular a raiz quadrada
    #Factorial: Usada para fazer a fatorisl de um número
                            #Apartir do momento que você botar import math, vai ser importado todos esses módulos acima


import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadro de {num} é {raiz}')

#Se você quer fazer o arredondamento do valor é só botar o módulo ciel

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')

#Se que você quer arredondar para baixo

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.floor(raiz)}')

#


