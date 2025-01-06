N1 = int(input("Informe o primeiro número: "))
N2 = int(input("Informe o segundo número: "))

if N1 > N2:
    print("O número %d  é maior que o número %d " % (N1, N2))
elif N2 > N1:
    print("O número %d  é maior que o número %d " % (N2, N1))
else:
    print("Os números são iguais")