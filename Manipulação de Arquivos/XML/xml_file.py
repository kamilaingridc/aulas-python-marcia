import xml.etree.ElementTree as ET


def xml_file():
    # parte1
    # elemento raiz
    root = ET.Element('Configs')

    # cria um elemento dentro da raiz
    general_config = ET.SubElement(root, 'Config')

    # adc um subelemento dentro do elemento
    version = ET.SubElement(general_config, 'Version')
    version.text = '1'  # use '=' em vez de '()'

    # parte2
    # cria árvore com o elemento raiz
    tree = ET.ElementTree(root)

    # parte3
    # salva em arquivo
    tree.write('config.xml')

    # lê o arquivo
    tree = ET.parse('config.xml')
    root = tree.getroot()

    # mostra a tree
    ET.dump(root)


xml_file()
