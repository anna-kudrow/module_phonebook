import text

def menu():
    for i, item in enumerate(text.main_menu):
        if i == 0:  # if not i:
            print(item)
        else:
            print(f'\t{i}. {item}')  
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 1 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.input_menu_error)       