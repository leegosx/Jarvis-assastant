from abc import ABC, abstractclassmethod

class UserInterface(ABC):
    @abstractclassmethod
    def show_address_book(self, address_book):
        pass
    
    
    @abstractclassmethod
    def show_notes(self, notes_book):
        pass
    
    
    @abstractclassmethod
    def show_command_help(self, commands):
        pass