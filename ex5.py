altura = float(input("Digite a altura em metros:"))
sexo = input("Digite o seu sexo:")

if (sexo == "homem" or sexo == "HOMEM" or sexo == "Homem"):
    peso_ideal = (72.7 * altura) - 58

elif (sexo == "mulher" or sexo == "Mulher" or sexo == "MULHER"):
    peso_ideal = (62.1 * altura) - 44.7 

print("O seu peso ideal é: {:.2f} KG".format(peso_ideal))


