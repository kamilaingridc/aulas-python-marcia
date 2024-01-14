#Peça um número para o usuário e imprima se ele é par ou ímpar. E se é múltiplo de 3 e se é múltiplo de 5#
num = int(input("Digite um número:"))
if num %2==0:
    print("É um número par")
else:
    print("É um número ímpar")
if num %3==0:
    print("É múltiplo de três")
else:
    print("Não é múltiplo de três")
if num%5==0:
    print("É múltiplo de cinco")
else:
    print("Não é múltiplo de cinco")