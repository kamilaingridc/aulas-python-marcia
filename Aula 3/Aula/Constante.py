pi = int(3.14)
raio = int(input("Digite o valor do raio:"))
altura = int(input("Digite o valor da altura:"))
area = 2*pi*raio*(raio+altura)
print(f"Área da base do cilindro: {area}")

volume = int(area*altura)
print(f"Volume do cilindro: {volume}")
