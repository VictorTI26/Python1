nota1 = float(input("Digita a primeira nota"))
nota2 = float(input("Digita a segunda nota"))

media = (nota1 + nota2)/2

if media>6:
    print("Aprovado")
elif media > 4 and media < 6 :
    print("Exame")
else :
    print("Reprovado")