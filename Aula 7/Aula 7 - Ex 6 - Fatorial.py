n = int(input("Fatorial de: ") )

resultado = 1
numero = 1

while numero <= n:
    resultado *= numero
    numero += 1

print(resultado)
