numero = int(input("Insira o valor a ser invertido: "))
numero = str(numero)

vetor = []

for i in numero:
    vetor.append(i)

print(vetor[::-1])
