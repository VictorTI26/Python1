D={"Aluno1": 7, "Aluno2": 6.5,"Aluno3": 8,"Aluno4": 7.5, "Aluno5": 3.5}

D.values()
notas = 0
for i in D.values():
    notas = notas + i

print(notas/5)


