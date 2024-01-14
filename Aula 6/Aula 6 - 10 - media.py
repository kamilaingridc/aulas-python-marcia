nota = float(input("Digite a nota da primeira prova: "))
print(f"A nota da primeira prova é {nota}.")
nota2 = float(input("Digite a nota da primeira prova: "))
print(f"A nota da primeira prova é {nota2}.")
nota3 = float(input("Digite a nota da primeira prova: "))
print(f"A nota da primeira prova é {nota3}.")

menor = min(nota, nota2, nota3)
soma = nota + nota2 + nota3
media = (soma - menor) / 2

print(f"A média das notas é: {media:.2f}")
