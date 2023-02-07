'''
Atividade: Listando
Todos os direitos reservados ©2022 Resilia Educação
➔ O QUE FAZER?
- Escrever um algoritmo que:
1. Cria duas listas de dez posições e;
2. Faça a multiplicação dos elementos de mesmo índice, colocando o resultado em uma terceira lista,
que deve ser mostrada como saída.
➔ COMO FAZER?
- Em grupos de 3 a 4 pessoas.
➔ FECHAMENTO
- Compartilhar onde sentiram mais dificuldade. 
'''

print("\n")
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
saida = [list1[0]*list2[0],
         list1[1]*list2[1],
         list1[2]*list2[2],
         list1[3]*list2[3],
         list1[4]*list2[4],
         list1[5]*list2[5],
         list1[6]*list2[6],
         list1[7]*list2[7],
         list1[8]*list2[8],
         list1[9]*list2[9]]
print("_"*60)         
print(f"O Resultado da multiplicação da lista 1 com a lista 2 é:")         
print(saida)
print("_"*60)   

