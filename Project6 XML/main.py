import xml.etree.ElementTree as ET
import local_en as local


def find_by_id(catalog, id):
    s = ''
    for book in catalog:
        if book.attrib['id'] == id:
            for attribute in book:
                s += attribute.tag + ': ' + attribute.text + '\n'
    if s:
        return s
    else:
        return None


def find_by_ISBN(catalog, ISBN):
    s = ''
    for book in catalog:
        if book[1].text == ISBN:
            for attribute in book:
                s += attribute.tag + ': ' + attribute.text + '\n'
    if s:
        return s
    else:
        return None


def count_number_of_books(catalog, year):
    n = 0
    for book in catalog:
        for attribute in book:
            if attribute.tag == 'Year_of_publishing' and attribute.text == year:
                n += 1
    return n


def count_average_value_of_books(catalog):
    publishing_houses = {}
    for book in catalog:
        children = {}
        for attribute in book:
            children[attribute.tag] = attribute.text
        if 'Publisher' in children and 'Price' in children:
            if children['Publisher'] in publishing_houses:
                publishing_houses[children['Publisher']].append(float(children['Price']))
            else:
                publishing_houses[children['Publisher']] = [float(children['Price'])]
    result = dict.fromkeys(publishing_houses.keys())
    for key in result:
        result[key] = sum(publishing_houses[key]) / len(publishing_houses[key])
    return result


def get_the_most_expensive_book(catalog, publisher, year):
    id = ''
    price = 0
    for book in catalog:
        children = {}
        for attribute in book:
            children[attribute.tag] = attribute.text
        if children['Publisher'] == publisher and children['Year_of_publishing'] == year and float(children['Price']) > price:
            price = float(children['Price'])
            id = book.attrib['id']
    if id:
        return find_by_id(catalog, id)
    else:
        return None


if __name__ == '__main__':
    tree = ET.parse('books.xml')
    catalog = tree.getroot()
    print(local.MENU)
    action = input(local.INPUT_ACTION)
    while action not in '12345':
        action = input(local.CORRECT_INPUT_ACTION)
    if action == '1':
        id = input(local.INPUT_ID)
        result = find_by_id(catalog, id)
        if result:
            print(result)
        else:
            print(local.NONEXISTENT_ID)
    elif action == '2':
        ISBN = input(local.INPUT_ISBN)
        result = find_by_ISBN(catalog, ISBN)
        if result:
            print(result)
        else:
            print(local.NONEXISTENT_ISBN)
    elif action == '3':
        year = input(local.INPUT_YEAR)
        print(count_number_of_books(catalog, year))
    elif action == '4 ':
        print(count_average_value_of_books(catalog))
    elif action == '5':
        list_of_publishers = []
        for book in catalog:
            for attribute in book:
                if attribute.tag == 'Publisher':
                    list_of_publishers.append(attribute.text)
        publisher = input(local.INPUT_PUBLISHER)
        while publisher not in list_of_publishers:
            publisher = input(local.NONEXISTENT_PUBLISHER)
        year = input(local.INPUT_YEAR)
        result = get_the_most_expensive_book(catalog, publisher, year)
        if result:
            print(result)
        else:
            print(local.NONEXISTENT_YEAR)
