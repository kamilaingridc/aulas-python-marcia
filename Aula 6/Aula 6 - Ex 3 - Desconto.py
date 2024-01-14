'''Calculadora de Desconto de Produto. Peça ao usuário que digite a quantidade de produtos a ser adquirido e o valor de cada unidade.
Caso a quantidade seja superior a 100 dê desconto de 10%, caso contrário dê desconto de 5%.
Exiba o valor inicial do produto, a quantidade solicitada, o desconto por unidade e o valor final a pagar. '''

quantidade = int(input("Digite a quantidade de produtos: "))
valor = float(input("Digite o valor de cada unidade: "))
if quantidade >= 100:
    desconto = quantidade * 0.10
else:
    desconto = quantidade * 0.5
total = quantidade * valor + desconto
print(f'O valor total é de {total}')