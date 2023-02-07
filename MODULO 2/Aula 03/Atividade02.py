'''
Atividade: Estruturar dado
Todos os direitos reservados ©2022 Resilia Educação
➔ O QUE FAZER?
- Crie um novo arquivo .py:
1. Elabore um algoritmo que leia uma lista de quinze números;
2. Remova os elementos ímpares;
3. Ordene e exiba em tela o menor e o maior valor que deve ser mostrado como saída.
➔ COMO FAZER?
- Em grupos de 3 a 4 pessoas.
➔ FECHAMENTO
- Compartilhar as experiências.
 '''

def eliminar_impares(lista):
    nova_lista = []
    for elemento in lista:
        if elemento % 2 == 0:
            nova_lista.append(elemento)
    return nova_lista


lista = [100, 1000, 1044, 1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 500, 12]
sem_os_impares = eliminar_impares(lista)
lista_ordenada = sorted(lista)

print("_"*75)
print("Lista Original: " + str(lista))
print("_"*75)
print("Sem os Impares: " + str(sem_os_impares))
print("_"*75)
print("Lista Ordenada: " + str(lista_ordenada))
print("_"*75)
print(max(int(number) for number in lista))
print("_"*75)
print(min(int(number) for number in lista))
print("_"*75)