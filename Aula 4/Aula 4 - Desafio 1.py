phrase = str(input("Digite uma frase: ")).strip().upper()
words = phrase.split()
junto = ''.join(words)
invert = junto[::-1]
'''invert = ''
for letter in range(len(junto) -1, -1, -1):
    invert += junto[letter] '''
print("O inverso de {} é {}".format(junto, invert))
print(junto, invert)
if invert == junto:
    print("True - É um palíndromo")
else:
    print("False - Não é um palíndromo")
