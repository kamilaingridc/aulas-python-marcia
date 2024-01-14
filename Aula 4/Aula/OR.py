idade = int(input("Qual sua idade: "))
CNH = str(input("Você tem Carteira de Habilitação? (S/N)")).lower()=="s"
Pode_dirigir = idade>=18 or CNH
print(Pode_dirigir)