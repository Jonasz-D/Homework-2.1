from files_utilities import *
from handler import facade_handler, end_program

LOGO = """
@@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@     @@@  @@@ @@@ @@@ 
@@@     @@@  @@@          @@@          @@@  @@@              @@@      @@@     @@@  @@@ @   @@@      @@@     
@@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@      @@@      @@@ @@@ @@@  @@@ @@@ @@@      @@@     
@@@     @@@          @@@          @@@  @@@          @@@      @@@      @@@     @@@  @@@   @ @@@      @@@     
@@@     @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@      @@@      @@@     @@@  @@@     @@@      @@@     

                                                                                   by Syntax Conquerors
"""

def main():
    print(LOGO)
    print('Type "help" to get a command list.')
    while True:
        command = input('\nEnter your command: ').lower()
        function_to_execute = facade_handler.function_runner(command)
        try:
            if function_to_execute == end_program:
                end_program()
                break
            else:
                function_to_execute()
        except:
            continue
            
if __name__ == '__main__':
    main()