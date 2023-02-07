# Em Python, listas de objetos são representadas pelo tipo list.
# Esse tipo de dados é basicamente uma sequência de elementos,
# que podem ou não ser do mesmo tipo.

# Vejamos alguns exemplos básicos de operações envolvendo listas.  #

# Cria uma lista sem nenhum elemento.
# A expressão lista_vazia = list() possui o mesmo efeito.

'''lista_vazia = []
print("Lista vazia: ", lista_vazia)
print("Tipo de uma lista: ", type(lista_vazia))

lista_inteiros = [10, 20, 30, 40]
print("Lista de inteiros: ", lista_inteiros)

lista_tipos_diferentes = ["George", "Orwell", 1984]
print("Lista de elementos com tipos diferentes: ", lista_tipos_diferentes)'''
###############     EXEMPLO    #######################################
#Lista vazia:  []
#Tipo de uma lista:  <class 'list'>
#Lista de inteiros:  [10, 20, 30, 40]
#Lista de elementos com tipos diferentes:  ['George', 'Orwell', 1984]
######################################################################

'''Python permite também a criação de listas aninhadas (uma lista dentro da outra). 
Este recurso é útil quando desejamos criar listas de várias dimensões (ou matrizes):'''

'''lista_aninhada = [1, [2, [3, [4]]], 5]
print("Lista aninhada: ", lista_aninhada)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3: ", matriz)
print("Matriz impressa de outra forma:")
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()'''
###############  EXEMPLO  ###########################
#  Lista aninhada:  [1, [2, [3, [4]]], 5]
#  Matriz 3x3:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  Matriz impressa de outra forma:
#  1 2 3
#  4 5 6
#  7 8 9
#####################################################

"""Percorrendo Listas
Linguagens de programação como C, C++ e Java usam índices para iterar sobre listas de elementos. 
Em Python, normalmente percorremos listas de elementos sem que existam índices associados a eles. 
Entretanto, em algumas situações desejamos percorrer uma lista (de números, por exemplo) em determinada ordem, 
índice por índice. Python nos permite fazer por meio de intervalos, usando a função range(), """

         # Sintaxe da função range().

'''inicio = 0
fim = 100
passo = 10

print(list(range(inicio, fim, passo)))# Convertendo um intervalo em uma lista.'''
##############  EXEMPLO   #####################
#  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
###############################################

'''Perceba que o elemento final do intervalo (no caso acima, o 100) não é retornado pela função range().
O exemplo abaixo mostra isso melhor. Além disso, se não fornecermos o passo, a função irá usar o valor padrão 1.'''

          # Ordenando listas.
'''lista = [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]
print("Lista não ordenada: ", lista)

lista.sort()
print("Lista ordenada: ", lista)

lista.sort(reverse=True)
print("Lista ordenada em ordem decrescente: ", lista)'''
####################   EXEMPLO   #############################################
#  Lista não ordenada:  [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]
#  L ista ordenada:  [-1, 2, 3, 7, 7, 15, 25, 30, 80, 100]
#  Lista ordenada em ordem decrescente:  [100, 80, 30, 25, 15, 7, 7, 3, 2, -1]
##############################################################################
'''Os exemplos acima mostram como ordenar listas em Python de forma forma que chamamos in place. 
Isso quer dizer que a lista foi ordenada sem que espaço adicional fosse usado.'''


'''Python nos permite também ordenar uma cópia da lista original e retornar essa cópia ordenada da lista. 
Assim, a lista original permanece inalterada e uma nova lista ordenada é criada e retornada. 
Veja como isso funciona:'''

    # Ordenando listas.
'''lista = [7, 2, 3, 7, -1, 9]
print("Lista original antes da ordenação: ", lista)

lista_ordenada = sorted(lista)
print("Lista ordenada: ", lista_ordenada)

print("A lista original permanece inalterada: ", lista)'''
#######################  EXEMPLO  ###########################
#  Lista original antes da ordenação:  [7, 2, 3, 7, -1, 9]
#  ista ordenada:  [-1, 2, 3, 7, 7, 9]
#  lista original permanece inalterada:  [7, 2, 3, 7, -1, 9]
##############################################################

'''A menos que você precise tanto da lista original quanto de uma cópia dessa lista ordenada, 
recomenda-se o uso da ordenação in place, uma vez que ela não cria uma lista nova, 
e portanto usa menos espaço em memória.'''

'''Modificando Listas'''
'''Em algumas situações, é preciso adicionar, remover ou modificar elementos em uma lista. 
ython nos provê recursos para fazer essas coisas. Veja:'''

    # Cria uma lista vazia.
'''lista = []

    # Adiciona elementos no final da lista.
lista.append("P")
lista.append("Y")
lista.append("T")
lista.append("H")
lista.append("O")
lista.append("N")

print(lista)'''



    #É possível modificar elementos em uma lista.
    # Dizemos que listas são tipos de dados mutáveis.
    # Este conceito ficará mais interessante quando estudarmos tuplas,
    # que são tipos de dados imutáveis.#

'''lista[1] = 'A'
lista[3] = 'R'
lista[4] = 'I'
lista[5] = 'A'

print(lista)'''