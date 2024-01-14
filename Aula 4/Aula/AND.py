usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
login = usuario == "user123"
login2 = senha == "456"
acesso = login and login2
print(acesso)