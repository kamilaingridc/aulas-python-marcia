n = int(input("Digite um número inteiro positivo: "))
qtd = 0

while n > 0:
    qtd += 1
    n //= 10

print(f"O número tem {qtd} dígitos.")
