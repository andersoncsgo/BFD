#questao 1
lista = [1, "teste", 1.25, []]
print(type(lista[3]))

#questao 2
#Usando a lista criada na questão anterior, use o método insert ou append para 
#adicionar mais dois elementos a lista e use remove, pop ou del para remover um 
#elemento da lista.
lista.insert(1, "adicionado")
print(lista)
lista.remove("adicionado")
print(lista)

#questao 3
#Faça uma cópia da lista da questão anterior. Use a função id para verificar se 
#realmente criou uma lista nova (obs: mesmo valor de ID indica que é o mesma lista 
#e não uma nova) 

lista1 = lista

print(id(lista1))
print(id(lista))

#Crie uma nova lista só com números (inteiro e/ou ponto flutuante) e multiplique os 
#elementos da lista por 5. O resultado deve ser uma nova lista com os elementos 
#multiplicados.

numeros = [1, 2, 3, 4]
multiplicacao = 5
numeros_multiplicados = [num * multiplicacao for num in numeros]
print(numeros_multiplicados)
print(numeros)

#questao 4
#Use o slice para criar uma nova lista que inclua apenas os elementos com índice 
#3 e 4 da lista a seguir:
lista2 = [1, 2, 3, 4, 5, 6]
nova_lista = lista2[3:5]
print(nova_lista)