n = int(input("Digite um número: "))

soma = 0

for digito in str(n):
    soma += int(digito)

print(f"A soma dos dígitos é: {soma}")

