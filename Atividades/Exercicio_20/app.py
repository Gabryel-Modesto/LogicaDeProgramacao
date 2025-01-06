age = int(input("Insira sua idade: "))

if age >= 18:
    print("Você é de maior")
elif age >= 12 and age <= 17:
    print("Você é um adolescente")
else:
    print("Você é uma criança")