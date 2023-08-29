phone_book = {}
PATH = 'module_phonebook/phones.txt'


def open_file():
    global phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip(). split(';')    
        phone_book[i] = contact


def save_file():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(';'.join([*contact]))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))    

def add_contact(new: list[str]):
    global phone_book
    c_id = max(phone_book) + 1 
    phone_book[c_id] = new

def search(word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for i, contact in phone_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[i] = contact
                break
    return result
