'''Verificação de Voto Obrigatório, Facultativo ou Não Eleitor.
Faça um programa que peça a idade do eleitor e informe qual o tipo de voto conforme as regras vigentes.'''
idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Não eleitor.")
elif idade <= 17:
    print("Facultativo")
else:
    print("Voto Obrigatório.")