n = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

p = float(input("Digite o peso da primeira nota: "))
p2 = float(input("Digite o peso da segunda nota: "))
p3 = float(input("Digite o peso da terceira nota: "))

media_ponderada = (n * p + n2 * p2 + n3 * p3) / (p + p2 + p3)
print(f"A média ponderada dessas notas é: {media_ponderada}")