#############################
####  PERCORRENDO LISTAS  ###
#############################
'''A maneira mais frequente de percorrer listas é utilizando o laço for. Com eles podemos
acessar os elementos de duas maneiras.'''
#lista_zeros = [0]*10
#for valor in lista_zeros:
#    print(valor)
'''
0
0
0
0
0
0
0
0
0
0
'''

#for i in range(len(lista_zeros)):
#    print(lista_zeros[i])
'''
0
0
0
0
0
0
0
0
0
0
'''

##################################
### Criando listas numéricas  ####
##################################
'''Uma maneira de popularmos uma lista com números é percorrê-la com range e
preencher índice a índice.'''
#lista_10x =[0]*10

#for i in = range(10):
#    lista_10x[i] = i*10

###########################################
#######  MÉTODOS DE LISTAS  ######
###########################################
'''
Métodos de listas: append
O método append acrescenta um elemento à última posição da lista.
'''   
lista = []
for i in range(2,11,2):
    lista.append(i)

'''
Métodos de listas: pop
O método pop remove um elemento de acordo com sua posição na lista. 
Caso não forneça um índice, ele remove e retorna o último elemento da lista.
'''  
valor = lista.pop(1)
últimoValor = lista.pop()
print(ùltimoValor, alor )