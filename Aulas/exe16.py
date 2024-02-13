def imprimir_com_numeracao(lista):
    for i, elemento in enumerate(lista):
        print(i+1,"-", elemento)

minha_lista = ["a", 10, True, "Olá"]
imprimir_com_numeracao(minha_lista)
