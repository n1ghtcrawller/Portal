import os
import xml.etree.ElementTree as ET


def getNameFromXML(XML_Path, tag):
    try:
        tree = ET.parse(XML_Path)
        root = tree.getroot()

        result = tree.findtext(f'.//{tag}')

    except IOError as e:
        print(e)
    print(''.join(str(result)))










