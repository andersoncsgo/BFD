"""
lista
"""

lista = []
print(type(lista))

frutas = ["limao", "banana", "morango", "coco"]
print(frutas)

#add elements
frutas.insert(1, "maca")
print(frutas[1])
frutas.append("kiwi")
print(frutas)

frutas_vermelhas = ["morango", "uva", "cereja", "amora", "framboesa"]

frutas+=frutas_vermelhas
print(frutas)

frutas.remove("morango")
print(frutas)

print("primeiro pop")
frutas.pop()
print(frutas)

print("segundo pop")
frutas.pop(4)
print(frutas)

print(frutas)


### copia de lista
print("---------")
frutas2 = frutas[:]
frutas2 = frutas.copy()
print(frutas2)
print(id(frutas))
print(id(frutas2))

frutas.index("limao")
print(frutas)