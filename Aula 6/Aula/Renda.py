'''Crie um programa em Python para um banco que avalia a elegibilidade de empréstimos com base na idade e renda mensal dos clientes. As regras são:
Clientes com 18 anos ou mais podem pedir um empréstimo se tiverem renda mensal acima de R$1500,00.
Menores de 18 anos podem obter um empréstimo se tiverem renda mensal acima de R$ 1000.
Utilize estruturas condicionais aninhadas para implementar essa análise e exiba se o cliente é elegível e sob qual condição.
'''
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))
if idade >= 18:
    if renda >= 1500:
        print("Você pode solicitar um empréstimo.")
    else:
        print("Você NÃO pode solicitar um empréstimo por renda menor do que requisitada.")
elif idade < 18:
    if renda > 1000:
        print("Você está elegível para solicitar um empréstimo com um responsável.")
    else:
        print("Você não tem renda o suficiente.")
else:
    print("Você não tem idade e nem saldo suficiente.")


