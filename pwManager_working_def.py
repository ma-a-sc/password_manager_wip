from sys import exit
from sys import argv
import json
import hashlib

# start parameters
script, filename = argv
# The function new_dict() replaces the dictionary in the .txt file with the 
# modified version that is created in this script.
# The function is usually called at the end of every action that alteres the 
# dictionary.
def new_dict():
    with open(filename, 'w') as file:
        file.write(json.dumps(text_file_dictionary))
# This parent class is only created for readability of the other classes and
# that they all are marked as commands.
class commands(object):

    def __init__(self):
        pass
    pass

# This class when called appends a new account linked to a password to the 
# dictionary that is stored in text_file_dictionary.
class append(commands):

    def __init__(self):
        self.account = input(
            "What is the Accountname you would like to append:\n> "
        )
        self.password = input(
            "To what account should the password be linked?\n> "
        )
        new_pw_dict = {self.account: self.password}
        text_file_dictionary.update(new_pw_dict)

        new_dict()

        exit()

# This class tells the user what password is used with the account that he/she
# requested.
class get_pw(commands):

    def __init__(self):
        self.account = input(
            "From which Account would you like to access the password?\n> "
        )
        
        print(text_file_dictionary.get(self.account))
    
# This class erases the account and password of a by the user set account.
class erase_pw(commands):

    def __init__(self):
        self.account_to_erase = input(
            """From what Account do you want to erase the"password and account?
            > """)
        
        text_file_dictionary.pop(account_to_erase)

        new_dict()

# This class changes the password of an account if the user correctly defines 
# an account that is allready present in the dictionary. If the account is not
# found in the dictionary the programms stops the process.
class change_pw(commands):

    def __init__(self):
        self.account = input(
            "What is the Accountname you would like to append:\n> "
            )
        if self.accountaccount in text_file_dictionary:
            password = input(
                "To what should the password be changed?\n> "
            )
            new_pw_dict = {self.account: password}
            text_file_dictionary.update(new_pw_dict)

            new_dict()
        
        else:
            print("Acount does not exits.")
            exit()

# This class clears the dictionary.
class erase_all_pws(commands):

    def __init__(self):
        self.sure = input("Are you sure you want to erase all passwords:\n> ")
        if self.sure == "yes":
            text_file_dictionary.clear()

            new_dict()


# opens the .txt file in which the passwords and account names are stored.
with open(filename, 'r') as m:
    contents = m.read()

with open("masterpw.txt") as v:
    master = v.read()
    print(master)

# the .txt file is not in a dictionary form so here I use json to convert the
# contents into a dictionary.
text_file_dictionary = json.loads(contents)

# asks the user for the masterpassword in order to access the application.
verification = input("What is the masterpassword?\n> ")

verification_d = verification.encode()

# need to hash the verification process
secure = hashlib.sha256()
secure.update(verification_d)
secure2 = secure.hexdigest()
print(secure2)

# checks if the correct masterpassword was given.
# encryption is lacking at this stage.
if secure2 == master:

    # asks the user which action he would like to perfom.
    command = input(
        """What action would you like to perform?\n
        Actions: append, get pw, erase pw, change pw, erase all pws\n> 
        """
        )

    # checks what action the user selected.
    if command == 'append':
        append()
    
    elif command == 'get pw':
        get_pw()
        
    elif command == 'erase pw':
        erase_pw()

    elif command == 'change pw':
        change_pw()

    elif command == 'erase all pws':
        erase_all_pws()
        
    else:
        print("I don't know this command.")
        e = input("Do you want to exit?")
        if e == "yes":
            exit()

else:
    print("Failed to log in.")
    exit()
