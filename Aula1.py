#len() Retorna o tamanho da string.
teste = "Apostila de Python"
len(teste)
18

#capitalize() Retorna a string com a primeira letra maiúscula
a = "python"
a.capitalize()
'Python'
count()

#Informa quantas vezes um caractere (ou uma sequência de caracteres) aparece na string.
b = "Linguagem Python"
b.count("n")
2

#startswith() Verifica se uma string inicia com uma determinada sequência.
c = "Python"
c.startswith("Py")
True

endswith()
#Verifica se uma string termina com uma determinada sequência.
d = "Python"
d.endswith("Py")
False

isalnum()
#Verifica se a string possui algum conteúdo alfanumérico (letra ou número).
e = "!@#$%"
e.isalnum()
False

isalpha()
#Verifica se a string possui apenas conteúdo alfabético.
f = "Python"
f.isalpha()
True

islower()
#Verifica se todas as letras de uma string são minúsculas.
g = "pytHon"
g.islower()
False

isupper()
#Verifica se todas as letras de uma string são maiúsculas.
h = "# PYTHON 12"
h.isupper()
True

lower()
#Retorna uma cópia da string trocando todas as letras para minúsculo.
i = "#PYTHON 3"
i.lower()
'#python 3'

upper()
#Retorna uma cópia da string trocando todas as letras para maiúsculo.
j = "Python"
j.upper()
'PYTHON'

swapcase()
#Inverte o conteúdo da string (Minúsculo / Maiúsculo).
k = "Python"
k.swapcase()
'pYTHON'

title()
#Converte para maiúsculo todas as primeiras letras de cada palavra da string.
l = "apostila de python"
l.title()
'Apostila De Python'

split()
#Transforma a string em uma lista, utilizando os espaços como referência.
m = "cana de açúcar"
m.split()
['cana', 'de', 'açúcar']

replace(S1, S2) 
#Substitui na string o trecho S1 pelo trecho S2.
n = "Apostila teste"
n.replace("teste", "Python")
'Apostila Python'

find()
#Retorna o índice da primeira ocorrência de um determinado caractere na string. Se o caractere não estiver na string retorna -1.
o = "Python"
o.find("h")
3

ljust()
#Ajusta a string para um tamanho mínimo, acrescentando espaços à direita se necessário.
p = " Python"
p.ljust(15)
' Python '

rjust()
#Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda se necessário.
q = "Python"
q.rjust(15)
' Python'

center()
#Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda e à direita, se necessário.
r = "Python"
r.center(10)
' Python '

lstrip()
#Remove todos os espaços em branco do lado esquerdo da string.
s = " Python "
s.lstrip()
'Python '

rstrip() 
#Remove todos os espaços em branco do lado direitoda string.
t = " Python "
t.rstrip()
' Python'

strip() 
#Remove todos os espaços em branco da string.
u = " Python "
u.strip()
'Python'

#Função Descrição Exemplo
#len retorna o tamanho da lista. L = [1, 2, 3, 4]
len(L) -> 4

#min retorna o menor valor da lista. L = [10, 40, 30, 20]
min(L) -> 10

#max retorna o maior valor da lista. L = [10, 40, 30, 20]
max(L) -> 40

#sum retorna soma dos elementos da lista. L = [10, 20, 30]
sum(L) -> 60

#append adiciona um novo valor na no final da lista.
L = [1, 2, 3]
L.append(100)
L -> [1, 2, 3, 100]

#extend insere uma lista no final de outra lista.
L = [0, 1, 2]
L.extend([3, 4, 5])
L -> [0, 1, 2, 3, 4, 5]

#del remove um elemento da lista, dado seu índice.
L = [1,2,3,4]
del L[1]
L -> [1, 3, 4]

#in verifica se um valor pertence à lista. L = [1, 2 , 3, 4]
3 in L -> True

#sort() ordena em ordem crescente
L = [3, 5, 2, 4, 1, 0]
L.sort()
L -> [0, 1, 2, 3, 4, 5]

#reverse() inverte os elementos de uma lista.
L = [0, 1, 2, 3, 4, 5]
L.reverse()
L -> [5, 4, 3, 2, 1, 0]

