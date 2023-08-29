import view
import text
import model

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.file_load_successful)
            case 2:
                pass
            case 3:
                book = model.phone_book
                view.show_book(book, text.empty_phone_book)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                view.print_message(text.end_program)
                break


