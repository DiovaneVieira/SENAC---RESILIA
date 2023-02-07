'''Segmentação de listas
Assim como as strings, listas também podem ser “cortadas” ou segmentadas em
pedaços menores. Essa operação é chamada de slice ou segmentação.'''

nomes = ['Jack', 'Brad', 'Leonardo', 'Natalie', 'Madonna']
print(nomes[1:3])

'''Cópias de listas
Atenção: atribuir uma lista a uma nova variável cria um “clone” em que alterações
refletem nos dois locais.
Cópias de listas devem ser feitas usando a operação de segmentação.'''

nomes = ['Jack', 'Brad', 'Leonardo', 'Natalie','Madonna']
lista_copia = nomes[:]
print(lista_copia)

'''Atividade: Pizzaiolo
Todos os direitos reservados ©2022 Resilia Educação
➔ O QUE FAZER?
- Escrever uma lista de suas pizzas favoritas e, em seguida, criar uma cópia chamada de
friend_pizzas. Então faça o seguinte:
- Adicionem uma nova pizza à lista original.
- Adicionem uma pizza diferente à lista friend_pizzas.
- Provem que vocês tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, exiba a primeira lista. Exiba a mensagem As pizzas favoritas
de meu amigo são:; em seguida, exiba a segunda lista. Certifique-se de que cada pizza
nova esteja armazenada na lista apropriada.'''