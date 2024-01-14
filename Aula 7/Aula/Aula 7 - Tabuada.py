#Faça um programa que peça ao usuário um número e imprima a tabuada desse número (até 10)#
tab = int(input("Enter a number to find the table: "))
for next in range(1, 11):
    print(tab, "x", next, "=", tab * next)