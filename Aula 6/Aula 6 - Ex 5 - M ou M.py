'''Determinar Maior e Menor Idade entre Três Pessoas.
Peça a idade de 3 pessoas e encontre a maior idade e a menor. Exiba essas informações. '''
idade = int(input("Qual a idade da primeira pessoa?"))
idade2 = int(input("Qual a idade da segunda pessoa?"))
idade3 = int(input("Qual a idade da terceira pessoa?"))
if idade > idade2 and idade > idade3:
    print("A maior idade é: ", idade)
elif idade2 > idade and idade2 > idade3:
    print("A maior idade é: ", idade2)
elif idade3 > idade and idade3 > idade2:
    print("Maior idade: ", idade3)
if idade < idade2 and idade < idade3:
    print("A menor idade é: ", idade)
elif idade2 < idade and idade2 < idade3:
    print("A maior idade é: ", idade2)
elif idade3 < idade and idade3 < idade2:
    print("A menor idade é: ", idade3)