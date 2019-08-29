import xml.etree.ElementTree as ET

def getMob(udidString):
    start = udidString.find('<dict>')
    end = udidString.find('</dict>')
    xml = udidString[start:end + 7]
    print(xml)
    root = ET.fromstring(xml)
    map = {}
    for index, item in enumerate(root):
        if item.tag == 'key':
            if root[index + 1].tag == 'string':
                map[item.text] = root[index + 1].text
    return map