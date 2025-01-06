wheels = int(input("Informe quantas rodas tem o veiculo: "))

if wheels > 2:
    print("Favor pagar o pedágio.")
elif wheels >= 1 or wheels <= 2:
    print("Pode passar livremente!")
else:
    print("Favor colocar um quantitativo de rodas válidos")