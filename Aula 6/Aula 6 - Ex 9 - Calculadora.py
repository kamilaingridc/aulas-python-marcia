escolha = int(input("Bem vinda a nossa calculadora!!\n"
      "Escolha qual operação matemática você quer: soma [1], subtração [2], multiplicação [3] ou divisão [4]: "))

print(f"Sua escolha foi {escolha}.")

num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num + num2
sub = num - num2
mult = num * num2
divisao = num / num2

if escolha == 1:
      print(f'A soma dos valores é: {soma}')
elif escolha == 2:
      print(f'A subtração dos valores é: {sub}')
elif escolha == 3:
      print(f'A multiplicação dos valores é: {mult}')
elif escolha == 4:
      print(f'A divisão dos valores é: {divisao}')
