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
                model.save_file()
                view.print_message(text.file_save_successful)
            case 3:
                book = model.phone_book
                view.show_book(book, text.empty_phone_book)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_message(text.contact_save_successful(contact[0]))
            case 5:
                request = view.input_request(text.for_search)
                result = model.search(request)
                view.show_book(result, text.not_search(request))
            case 6:
                pass
            case 7:
                pass
            case 8:
                view.print_message(text.end_program)
                break


