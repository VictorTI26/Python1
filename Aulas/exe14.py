numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
    print("Tabuada do {numero}:")
    for i in range(1, 11):
        print("{numero} x {i} = {numero * i}")
else:
    print("Número fora do intervalo válido.")
