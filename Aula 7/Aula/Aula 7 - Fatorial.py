numero = int(input("Digite um número: "))
fatorial = 1
next = 1
while next <= numero:
    fatorial *= next
    next += 1
print("Fatorial de", numero, "é:", fatorial)