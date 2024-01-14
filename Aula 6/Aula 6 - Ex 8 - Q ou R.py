ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
ladoC = float(input("Digite o valor do lado C: "))
ladoD = float(input("Digite o valor do lado D: "))

if ladoA == ladoB and ladoA == ladoC and ladoA == ladoD:
    print("É quadrado.")
elif ladoA == ladoB and ladoC == ladoD or ladoA == ladoD and ladoC == ladoB or ladoB == ladoD and ladoC == ladoA:
    print("É retângulo.")
else:
    print("Não é retângulo e nem quadrado.")
