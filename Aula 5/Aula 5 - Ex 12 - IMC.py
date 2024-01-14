peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite a sua altura (M): "))
imc = peso / (altura*altura)
print("Seu IMC é %.2f" % imc)