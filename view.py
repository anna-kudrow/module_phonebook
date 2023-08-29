import text

def menu():
    for i, item in enumerate(text.main_menu):
        if i == 0:  # if not i:
            print(item)
        else:
            print(f'\t{i}. {item}')  
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.input_menu_error)       


def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')      


def show_book(book: dict, msg: str) -> bool:
    if book:
        print('\n' + '=' * 67)
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')     
        print('=' * 67 + '\n')  
    else:
        print_message(msg)    
 