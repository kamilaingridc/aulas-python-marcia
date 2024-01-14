import random
cont = "SIM"
while cont == "SIM":
    usuario = input("Escolha Pedra, Papel ou Tesoura: ").lower()
    computer = random.choice(["pedra", "papel", "tesoura"])
    print("Você escolheu", usuario)
    print("Computador escolheu", computer)
    if usuario == computer:
        print("Empate!")
    elif usuario == "papel" and computer == "pedra":
        print("Usuário ganhou!")
    elif usuario == "papel" and computer == "tesoura":
        print("Computador ganhou!")
    elif usuario == "pedra" and computer == "tesoura":
        print("Usuário ganhou!")
    elif usuario == "tesoura" and computer == "papel":
        print("Usuário ganhou!")
    elif usuario == "tesoura" and computer == "pedra":
        print("Computador ganhou!")
    elif computer == "papel" and usuario == "pedra":
        print("Usuário ganhou!")
    elif computer == "pedra" and usuario == "tesoura":
        print("Computador ganhou!")
    elif computer == "tesoura" and usuario == "papel":
        print("Computador ganhou!")
    else:
        print("Informação incorreta. Digite novamente!")

    cont = input("Você quer jogar novamente? (SIM/NÃO) \n").upper()
