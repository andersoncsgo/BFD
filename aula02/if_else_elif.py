idade_cliente = int(input("informe a idade do cliente: "))

if idade_cliente < 18:
    print("Cliente menor de idade, meia entrada")
elif idade_cliente >= 60:
    print("Cliente cortesia")
else:
    print("Cliente sem cortesia")