lado = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado == lado2 == lado3:
    print("É um triângulo equilátero.")
elif lado == lado2 or lado2 == lado3 or lado == lado3:
    print("É um triângulo isóceles.")
else:
    print("É um triângulo escaleno.")