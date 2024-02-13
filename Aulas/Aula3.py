#função
def maior (x, y):
    if x>y:
        print (x)
    else:
        print(y)

#exemplo 1
def soma(x,y):
 total = x+y
 print("Total soma = ",total)
#programa principal
total = 10
soma(3,5)
print("Total principal = ",total)

#Exemplo2
def soma(x,y):
 global total2
 total2 = x+y
 print("Total soma = ",total)
#programa principal
global total2
total = 10
soma(3,5)
print("Total principal = ",total)


#Retorno de valores
def soma(x,y):
 total = x+y
 return total

#programa principal
s=soma(3,5)
print("soma = ",s)

#valor padrão
def calcula_juros(valor, taxa=10):
 juros = valor*taxa/100
 return juros
print(calcula_juros(500))




