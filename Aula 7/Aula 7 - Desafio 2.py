taxa_reproducao = float(input("Digite a taxa de reprodução (como um número decimal): "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade (como um número decimal): "))
coelhos_iniciais = int(input("Digite o número inicial de coelhos: "))
geracoes = int(input("Digite o número de gerações a simular: "))

populacao = coelhos_iniciais

for geracao in range(geracoes):
    coelhos_nascidos = int(populacao * taxa_reproducao)
    coelhos_mortos = int(populacao * taxa_mortalidade)

    populacao = populacao + coelhos_nascidos - coelhos_mortos

    print(f"Geração {geracao+1}: {populacao} coelhos")

print(f"A população de coelhos após {geracoes} gerações é de {populacao} coelhos.")
