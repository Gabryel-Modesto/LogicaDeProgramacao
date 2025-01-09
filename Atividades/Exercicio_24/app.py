N1 = int(input("Olá, informe um número: "))
N2 = int(input("Informe outro número: "))

multiplication = N1 * N2 

if multiplication <= 100:
    print("O número informado é: %d, consideirado baixo  " % (multiplication))
else:
    print("O número informado é: %d, consideirado alto " % (multiplication))