n = int(input("Digite um número natural (N): "))
print(f"O número digitado foi {n}")

soma = 0
numero = 1
while numero <= n:
    soma += numero
    numero += 1

print(f'A soma dos número naturais {n} é: {soma}')
