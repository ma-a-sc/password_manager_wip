from sys import exit
from sys import argv
import json

script, filename = argv

with open(filename, 'r') as m:
    contents = m.read()

text_file_dictionary = json.loads(contents)

verification = input("What is the Master Password.\n> ")

if verification == "Masterpassword":
    command = input(
        """What action would you like to perform?\n
        Actions: append, get pw, erase pw, change pw, erase all pws\n> 
        """
        )
    
    if command == 'append':
        account = input(
            "What is the Accountname you would like to append:\n> "
            )
        password = input(
            "To what account should the password be linked?\n> "
            )
        new_pw_dict = {account: password}
        text_file_dictionary.update(new_pw_dict)

        with open(filename, 'w') as file:
            file.write(json.dumps(text_file_dictionary))
        
        exit()
    
    elif command == 'get pw':
        account = input(
            "From which Account would you like to access the password?\n> "
        )
        
        print(text_file_dictionary.get(account))
        
    elif command == 'erase pw':
        account_to_erase = input(
            """From what Account do you want to erase the"password and account?
            > """)
        
        text_file_dictionary.pop(account_to_erase)

        with open(filename, 'w') as file:
            file.write(json.dumps(text_file_dictionary))

    elif command == 'change pw':
        account = input(
            "What is the Accountname you would like to append:\n> "
            )
        if account in text_file_dictionary:
            password = input(
                "To what should the password be changed?\n> "
            )
            new_pw_dict = {account: password}
            text_file_dictionary.update(new_pw_dict)

            with open(filename, 'w') as file:
                file.write(json.dumps(text_file_dictionary))
        
        else:
            print("Acount does not exits.")
            exit()


    elif command == 'erase all pws':
        sure = input("Are you sure you want to erase all passwords:\n> ")
        if sure == "yes":
            text_file_dictionary.clear()

            with open(filename, 'w') as file:
                file.write(json.dumps(text_file_dictionary))
        
    else:
        print("I don't know this command.")
        e = input("Do you want to exit?")
        if e == "yes":
            exit()

else:
    exit()





