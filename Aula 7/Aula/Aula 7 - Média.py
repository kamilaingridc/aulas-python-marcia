#Faça um programa que exiba a média de uma lista de números (tamanho da lista é definido pelo usuário)#
med = int(input("Digite o tamanho da sua lista: "))
tam = []
for next in range(med):
    num = float(input("Digite um número: "))
    tam.append(num)
media = sum(tam)/med
print("A média dos números é:", media)
