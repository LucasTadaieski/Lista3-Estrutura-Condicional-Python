numero = int(input("Digite um número:"))


if(numero %2 == 0 and numero %3 == 0):
    divisao2 = numero /2
    divisao3 = numero /3
    print("Sim, o número é divisivel por 2 e 3, o resultado respectivamente é: {}, {}".format(divisao2, divisao3))

elif(numero %5 == 0):
        divisao5 = numero /5
        print("Sim, o número é divisivel por 5, o resultado é: {}".format(divisao5))

elif(numero %7 == 0):
        divisao7 = numero /7
        print("Sim, o número é divisivel por 7, o resultado é: {}".format(divisao7))
