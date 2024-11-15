import xml.etree.ElementTree as ET
import json


def parse_xml():
    tree = ET.parse('cats.xml')
    root = tree.getroot()

    facts = []

    for child in root:
        print(child.tag, child.attrib)
        for grandchild in child:
            if grandchild.tag == 'fact':
               facts.append(grandchild.text)
    print(facts)

    with open('cats.txt', mode='w')as f:
        f.write('\n'.join(facts))

def parse_xml_2():
    tree = ET.parse('cats.xml')
    root = tree.getroot()

    facts =[]

    for info in root.findall('info'):
        fact = info.find('fact').text
        facts.append(fact)

        with open('cats2.txt', mode='w') as f:
            f.write('\n'.join(facts))


def example_json():
    tree = ET.parse('cats.xml')
    root = tree.getroot()

    facts = []

    for info in root.findall('info'):
        fact = info.find('fact').text
        facts.append({"fact":fact})

        #facts.append(fact) als mögliche Variante statt facts.append ({"fact":fact})

    with open('cats.json', mode='w') as f:
        json.dump(facts, f , indent=4)

def read_json():
    with open('cats.json', mode=r) as f:
        data = json.load(f)
        print(data, type(data))


def compare():
    def example_json():
        tree = ET.parse('cats.xml')
        root = tree.getroot()

        facts = {}

        for index, info in enumerate (root.findall('info'),1):
            fact = info.find('fact').text
            facts[index] = {'fact':fact}

            facts.append(fact)

        print(type(facts), facts)
        with open('cats.json', mode='w') as f:
            json.dump(facts, f, indent=4)

        with open('cats.json', mode='r') as f:
            new_facts = json.load(f)

        print(type(new_facts), new_facts)

        print(facts == new_facts)

#if __name__ == '__main__':
    # parse_xml()
    # parse_xml_2()
    # example_json()
    # read_json()
    #compare()

if __name__ == '__main__':
    parse_xml()