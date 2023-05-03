numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

soma = numero1 + numero2 

if (soma >= 30 and numero1 > numero2):
    print("O resultado da soma é: {}, o maior número é: {}".format (soma, numero1))

elif (soma >= 30 and numero2 > numero1):
    print("O resultado da soma é: {}, o maior número é: {}".format (soma, numero2))

else:
    print("O resultado da soma é:", soma)
