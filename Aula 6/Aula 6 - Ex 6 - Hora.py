'''Verificação de Hora Válida. Peça que o usuário digite a hora, os minutos e os segundos.
Verifique se todos os números estão nos intervalos corretos (exemplo: a hora deve ser maior ou igual a zero e menor que 24).
Exiba se a hora é válida ou inválida. '''
hora = int(input("Digite as horas:"))
min = int(input("Digite os minutos:"))
seg = int(input("Digite os segundos:"))
if hora >= 0 and hora <24 and min >= 0 and min <60 and seg >=0 and seg < 60:
    print("Hora válida.")
else:
    print("Hora inválida.")

