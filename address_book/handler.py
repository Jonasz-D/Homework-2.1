from functions import *

class FacadeHandler:
    def __init__(self, commands):
        self.commands = commands

    def function_runner(self, command):
        if command == 'help':
            return accepted_commands(self.commands)
        elif command in self.commands:
            return self.commands[command]  
        else:
            return unknown_command

def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    'add contact': add_contact,
    'delete contact': delete_contact,
    'add phone': add_phone,
    'change phone': change_phone_num,
    'delete phone': delete_phone,
    'add email': add_email,
    'change email': change_email,
    'delete email': delete_email,
    'add birthday' : set_birthday,
    'birthday': days_to_birthday,
    'add address': add_address,
    'change address': change_address,
    'delete address': delete_address,
    'add note': add_note,
    'edit note': edit_note,
    'delete note': remove_note,
    'show notes':show_notes,
    'find note': search_note_by_tags,
    'show all': show_all,
    'find contact' : find_contact,
    'sort folder': sort_folder,
    'save': save_to_file,
    'exit': end_program,
    'help': accepted_commands, 
    }
    return commands


facade_handler = FacadeHandler(input_parser())
        