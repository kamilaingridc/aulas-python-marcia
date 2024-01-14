'''Jogo de Adivinhação. Crie um jogo de adivinhação em que o programa escolhe um número aleatório entre 1 e 10,
 e o jogador precisa tentar adivinhar qual é esse número. O programa deve fornecer dicas ao jogador indicando
 se o número é maior ou menor do que o palpite atual. O jogador tem 2 chances de acertar o número.
 Faça utilizando somente a condicional, não utilize loop (while ou for).
DICA: Utilize a biblioteca Random e a função random.randint '''

import random
import time

numero_sorteado = random.randint(1,10)

print("Bem-vindo ao nosso jogo de adivinhação!\n"
      "Você terá duas chances e terá de adivinhar um número entre 1 e 10.\n"
      "Boa sorte!\n")

n = int(input("Digite a primeira tentativa: "))
print(f"Você chutou o número {n}. Será que acertou?")
time.sleep(1)
if n == numero_sorteado:
    print("Parabéns! Você acertou.")
    time.sleep(1)
else:
    if n < numero_sorteado:
        print("Ainda não... O número é maior.")
        time.sleep(1)
    else:
        print("Ainda não... O número é menor.")
        time.sleep(1)

n2 = int(input("Digite a segunda e última tentativa: "))

if n2 == numero_sorteado:
    print("Parabéns! Você acertou.")
    time.sleep(1)
else:
    print(f"Você perdeu :(. O número era {numero_sorteado}.")