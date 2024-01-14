str("Sua data de aniversário é:{0}/{1},{2}")
dia = int \
    (input("Digite o dia do seu aniversário:"))
if dia > 31:
    print("O número deve ser igual ou menor que 31")
mes = int \
    (input("Digite o mês do seu aniversário:"))
if mes > 12:
            print('O número deve ser igual ou menor que 12')
ano = int \
    (input("Digite o ano do seu aniversário:"))
if ano > 9999:
            print("O número deve ter 4 dígitos")

data = format(str, dia, mes, ano)
print(data)