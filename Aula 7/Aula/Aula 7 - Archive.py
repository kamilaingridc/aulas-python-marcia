archive = "C:/Users/Public/Archive.txt"
with open(archive, "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
