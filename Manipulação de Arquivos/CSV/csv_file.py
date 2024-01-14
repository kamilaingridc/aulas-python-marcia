import csv
# importa biblioteca csv


def csv_file():
    # abre e cria um arquivo csv
    with open('products.csv', 'w', newline='') as archive:
        writer = csv.writer(archive)
        # coloca o cabeçalho e da valor a eles
        writer.writerow(["Name", "Price"])
        writer.writerow(["Book", 20])
    # le o arquivo
    with open('products.csv', 'r') as archive:
        reader = csv.reader(archive)
        for row in reader:
            print(row)


csv_file()
