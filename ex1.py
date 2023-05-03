numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo numero:"))

if(numero1>numero2):
    diferença = (numero1 - numero2)
    print("O maior numero é:{} e a diferença entre eles é: {}".format(numero1, diferença)) 

else:
    diferença = (numero2 - numero1)
    print("O maior numero é:{} e a diferença entre eles é: {}".format(numero2, diferença)) 