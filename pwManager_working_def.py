from sys import exit
from sys import argv
import json
import hashlib
from cryptography.fernet import Fernet

# start parameters
script, filename = argv
# The function new_dict() replaces the dictionary in the .txt file with the 
# modified version that is created in this script.
# The function is usually called at the end of every action that alteres the 
# dictionary.
def new_dict():
    with open(filename, 'w') as file:
        file.write(json.dumps(text_file_dictionary))

def erase_file_new_content(file_to_change, new_content):
    with open(file_to_change, 'w') as file_to_c:
        file_to_c.write(new_content)

def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string

def fernet_string_encrypting(string_to_encrypt, fernet_key):

    f = Fernet(fernet_key)
    string_to_encrypt_b = string_to_encrypt.encode()
    token = f.encrypt(string_to_encrypt_b)

    return token

def fernet_string_decrypting(string_to_decrypt, fernet_key):

    f = Fernet(fernet_key)
    string_to_decrypt_b = string_to_decrypt.encode()
    decrypted_string = f.decrypt(string_to_decrypt_b)

    return decrypted_string

def password_to_decrypt(input_user):
    password_to_decrypt_decrypted = fernet_string_decrypting(input_user, fernet_key)
    password_to_decrypt_decrypted_d = password_to_decrypt_decrypted.decode()

    return password_to_decrypt_decrypted_d

def password_to_encrypt(input_user):
    password_fer = fernet_string_encrypting(input_user, fernet_key)
    password_fer_encoded = password_fer.decode()

    return password_fer_encoded

def new_master_password(new_master):
    new_master_hash = string_to_hash_func(new_master)

    erase_file_new_content("masterpw.txt", new_master_hash)


# This parent class is only created for readability of the other classes and
# that they all are marked as commands.
class commands(object):

    def __init__(self):
        pass
    pass

# This class when called appends a new account linked to a password to the 
# dictionary that is stored in text_file_dictionary.
# !Need to check if the account is allready defined. If so I have to ask the 
# user to use the change pw action instead.
class append(commands):

    ## In this I only have to encode the string not decode

    def __init__(self):
        self.account = input(
            "What is the Accountname you would like to append:\n> "
        )
        self.password = input(
            "To what account should the password be linked?\n> "
        )

        encrypted_password = password_to_encrypt(self.password)

        new_pw_dict = {self.account: encrypted_password}
        text_file_dictionary.update(new_pw_dict)

        new_dict()

        exit()

# This class tells the user what password is used with the account that he/she
# requested.
class get_pw(commands):

    ## here I have to encrypted the input the user gives and check the dictionary
    ## for the value. The value has to be decrypted.

    def __init__(self):
        self.account = input(
            "From which Account would you like to access the password?\n> "
        )

        password_to_de = text_file_dictionary.get(self.account)

        password_de = password_to_decrypt(password_de)

        print(password_de)

    
# This class erases the account and password of a by the user set account.
class erase_acc_pw(commands):

    #Same precediure as with the get_pw

    def __init__(self):
        self.account_to_erase = input("""
            Which account and password would you like to erase? Pls put in the
            accountname.\n> 
            """)
        
        account_erase = text_file_dictionary.get(self.account_to_erase)
        
        text_file_dictionary.pop(account_erase)

        new_dict()

# This class changes the password of an account if the user correctly defines 
# an account that is allready present in the dictionary. If the account is not
# found in the dictionary the programms stops the process.
class change_pw(commands):
    ## Get the input from the user, erase the old one and set the new one that 
    ## needs to be encypted.

    def __init__(self):
        self.account = input(
            "What is the Accountname you would like to append:\n> "
            )

        if self.account in text_file_dictionary:
            password = input(
                "To what should the password be changed?\n> "
            )

            ## here we need a function to encrypt the password

            new_password = password_to_encrypt(password)

            new_pw_dict = {self.account: new_password}
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

            sure_sure = input("Are you certain?")

            if sure_sure == "yes":
                text_file_dictionary.clear()

                new_dict()

            else:
                exit()
        
        else:
            exit()


# asks the user for the masterpassword in order to access the application.
verification = input("What is the masterpassword?\n> ")

masterpassword_hash = string_to_hash_func(verification)

with open("masterpw.txt") as v:
    master = v.read()

# runs the entered masterpassword through the sha256 algorythm.
# checks if the correct masterpassword was given.
# encryption is lacking at this stage.
if masterpassword_hash == master:
    fernet_key = input("Pls insert decoding key.\n>")

    # opens the .txt file in which the passwords and account names are stored.
    with open(filename, 'r') as m:
        contents = m.read()

    # the .txt file is not in a dictionary form so here I use json to convert the
    # contents into a dictionary.
    text_file_dictionary = json.loads(contents)

    # asks the user which action he would like to perfom.
    command = input("""
        What action would you like to perform?\n
        Actions: append, get pw, erase acc and pw, change pw, erase all pws,
        change masterpassword\n> 
        """)

    # checks what action the user selected.
    if command == 'append':
        append()
    
    elif command == 'get pw':
        get_pw()
        
    elif command == 'erase acc and pw':
        erase_acc_pw()

    elif command == 'change pw':
        change_pw()

    elif command == 'erase all pws':
        erase_all_pws()

    elif command == 'change masterpassword':
        change_verification = input("What is the masterpassword?\n> ")

        change_secure2 = string_to_hash_func(change_verification)

        if change_secure2 == master:
            
            new_master = input(
                "What should be the new masterpassword be set to?\n>"
                )

            new_master_password(new_master)

        else:
            exit()

    else:
        print("I don't know this command.")
        ex = input("Do you want to exit?")
        if ex == "yes":
            exit()

else:
    print("Failed to log in.")
    exit()
