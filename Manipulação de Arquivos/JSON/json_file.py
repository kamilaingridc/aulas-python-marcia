import json
# importa a biblioteca json


def json_file():
    # define o conteúdo do arquivo separando por :
    data = {"Name": "João", "Age": 25, "Profession": "Engineer"}
    # abre arquivo json que foi ja atribuido conteúdo
    with open('data.json', 'w') as archive:
        json.dump(data, archive)
    # le arquivo json
    with open('data.json', 'r') as archive:
        print(json.load(archive))


json_file()
