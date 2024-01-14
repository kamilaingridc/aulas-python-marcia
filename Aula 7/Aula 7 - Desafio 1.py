def desenhar_forca(erro):
    partes_forca = [
        """
           ------
           |    |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    print(partes_forca[erro])

def jogo_da_forca():
    palavra = input("Jogador 1, escolha uma palavra: ").lower()
    tentativas_restantes = 6
    letras_corretas = []
    letras_erradas = []

    while tentativas_restantes > 0:
        letra = input("Jogador 2, insira uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira apenas uma letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            if set(letras_corretas) == set(palavra):
                print(f"Parabéns! Você acertou a palavra: {palavra}")
                break
        else:
            letras_erradas.append(letra)
            tentativas_restantes -= 1

        desenhar_forca(6 - tentativas_restantes)
        print(f"Letras corretas: {', '.join(letras_corretas)}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")

    if tentativas_restantes == 0:
        print(f"Você perdeu! A palavra era: {palavra}")

jogo_da_forca()
