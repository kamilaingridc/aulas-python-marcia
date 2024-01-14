'''Calcule o resultado e o resto da divisão entre o dividendo e o divisor. Exiba todas as informações.'''
n = int(input("Digite o número dividendo: "))
print(f'O número {n} é o dividendo.')
n2 = int(input("Digite o número divisor: "))
print(f'O número {n2} é o divisor.')
resultado = n/n2
resto = n % n2
print(f'O resultado da divisão é {resultado} e o resto da divisão é {resto}.')
