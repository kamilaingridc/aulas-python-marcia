credencial = input("Digite seu acesso: ")
acesso = "adm"
autorizacao = input("Autorizado pelo supervisor? (S/N): ")
login = (credencial.lower()).strip() == acesso and autorizacao.lower() == "s"
print(login)

