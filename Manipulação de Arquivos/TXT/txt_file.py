def txt_file():
    # cria e abre o arquivo
    with open('meu_arquivo.txt', 'w') as archive:
        # escreve no arquivo direto do pycharm
        archive.write('Olá, mundo!\n'
                      'Python é divertido!')
    # le o arquivo
    with open('meu_arquivo.txt', 'r') as archive:
        content = archive.read()
    # printa o conteúdo
    print(content)


# chama a função
txt_file()
