opcao = input("Digite a opção desejada:(F/C)")
graus = float(input("Digite os graus:"))
if opcao.upper() == "C":
    print(f'C para F:{(graus*1.8)+32}')
elif opcao.upper() == "F":
    print(f'F para C:{(graus-32)/1.8}')
else:
    print("Informação incorreta")