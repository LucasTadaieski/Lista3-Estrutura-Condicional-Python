salario = float(input("Digite o valor do salário:"))
prestaçao = float(input("Digite o valor da prestação do empréstimo:"))

if (prestaçao >  (salario*0.20)):
    print ("Empréstimo não concedido")

else:
    print ("Empréstimo concedido")