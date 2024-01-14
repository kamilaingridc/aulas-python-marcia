nota = float(input("Digite a nota da prova (0 a 10): "))

if 9 <= nota <= 10:
    print('Sua nota é A')
elif 7 <= nota < 9:
    print('Sua nota é B')
elif 5 <= nota < 7:
    print('Sua nota é C')
elif 3 <= nota < 5:
    print('Sua nota é D')
elif 0 <= nota < 3:
    print('Sua nota é E')
else:
    print('Nota inválida')

if 0 > nota > 10:
    print("Nota inválida")
