#Peça 5 números para o usuário imprima qual o maior#
'''
num = float(input("Digite um número:"))
num2 = float(input("Digite um número:"))
num3 = float(input("Digite um número:"))
num4 = float(input("Digite um número:"))
num5 = float(input("Digite um número:"))

if num > num2:
    maior = num
else:
    maior = num2
if maior < num3:
    maior = num3
if maior < num4:
    maior = num4
if maior < num5:
    maior = num5
print(f"Esse é o maior número: {maior}")
'''
num = float(input("Digite um número:"))
num2 = float(input("Digite um número:"))
num3 = float(input("Digite um número:"))
num4 = float(input("Digite um número:"))
num5 = float(input("Digite um número:"))
list = [num, num2, num3, num4, num5]
print("O menor número da lista é:", (min(list)))
print("O maior número da lista é:", (max(list)))