phone_book = {}
PATH = 'module_phonebook/phones.txt'


def open_file():
    global phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip(). split(';')    
        phone_book[i] = contact