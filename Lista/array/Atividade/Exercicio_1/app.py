arrNotas = [8, 5, 9, 4, 6]

i = 0
somaNotas = 0

while i < 5:
    somaNotas = somaNotas + arrNotas[i]
    i = i + 1
    
media = somaNotas / 5
print("Media do aluno foi: %.1f " % media)