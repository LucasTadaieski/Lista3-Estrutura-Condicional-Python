#Recebe os Dados
peso = float(input("Digite o seu peso (em KG): "))
altura = float(input("Digite a sua altura (em metros): "))

#Calcula o valor do IMC e exibe o resultado
imc = peso / (altura**2)
print("O resultado do IMC é de: {:.2f}".format(imc))

#Verifica a condição e exibe os resultados 
if (imc < 18.5):
    print("O resultado do seu IMC deu abaixo do peso")

elif (imc >= 18.5 and imc <= 25):
    print("O resultado do seu IMC deu peso normal")

elif (imc > 25 and imc <= 30):
    print("O resultado do seu IMC deu acima do peso")

elif (imc > 30):
    print("O resultado do seu IMC deu Obeso")

