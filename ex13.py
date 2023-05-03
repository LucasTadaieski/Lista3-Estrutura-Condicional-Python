#Entrada de Dados
a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

#Faz a Operação de Soma A + B
soma = a + b

#Exibe o Resultado
if(soma < c):
    print("A soma de A + B = {}, é menor que o valor de C".format(soma))

elif(soma > c):
    print("A soma de A + B = {}, é maior que o valor de C".format(soma))