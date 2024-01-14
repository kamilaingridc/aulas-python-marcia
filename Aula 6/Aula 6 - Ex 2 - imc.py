peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite sua altura (M): "))
imc = peso / (altura * altura)
print(f"O seu IMC é {imc:.02f}")
if imc <= 18.5:
    print("Abaixo do peso.")
elif imc <= 24.9:
    print("Normal.")
elif imc <= 29.9:
    print("Sobrepeso. Cuidado!")
elif imc <= 34.9:
    print("Obesidade.")
elif imc <= 39.9:
    print("Obesidade mórbida.")
else:
    print("Obesidade mórbida.")