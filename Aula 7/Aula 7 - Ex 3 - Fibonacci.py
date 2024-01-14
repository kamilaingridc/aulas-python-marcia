n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1

if (n==1) or (n==2):
    print("1")
else:
    for numero in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
print(f'O termo na Série de Fibonacci é: {termo} ')