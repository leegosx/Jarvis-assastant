from user_interface import UserInterface

class ConsoleUI(UserInterface):
    def show_address_book(self, address_book):
        for contact in address_book:
            print(contact)
        
    
    def show_notes(self, notes_book):
        for note in notes_book:
            print(note)
        
    
    def show_command_help(self, commands):
        for command in commands:
            print(command['name'] + ": " + command['description'])