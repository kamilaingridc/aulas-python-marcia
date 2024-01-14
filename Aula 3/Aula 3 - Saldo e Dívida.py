saldo = float(input("Valor do saldo: "))
divida = float(input("Valor da dívida: "))
frase = f"Seu saldo é de R${saldo} e sua dívida é de R${divida}"
if saldo < divida:
    print("Você está devendo mais do que você tem!")
else:
    print("Saldo suficiente.")
print(frase)
