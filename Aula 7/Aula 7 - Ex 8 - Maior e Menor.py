maior = float('-inf')
menor = float('inf')
contador = 1

while contador <= 5:
    numero = float(input("Digite um número: "))

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    contador += 1

print(f"O maior número é: {maior} e o menor número é {menor}")
