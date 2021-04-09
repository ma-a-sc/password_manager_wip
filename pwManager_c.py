import dict_functions
import encryption_functions

# Adds a new key value pair to the dictionary after encrypting the password
# input from the user. Writes the new pair into the pw.txt file.
def append_pw(fernet_key, text_file_dictionary):
    account = input(
    "\nWhat is the Accountname you would like to append:\n>"
    )
    password = input(
    "\nTo what account should the password be linked?\n>"
    )

    encrypted_password = encryption_functions.input_to_encrypt(password, fernet_key)

    new_pw_dict = {account: encrypted_password}
    text_file_dictionary.update(new_pw_dict)

    dict_functions.new_dict(text_file_dictionary)


# Searches the dictionary for a key and decrypts the value. Prints out the value.
def get_pw_(fernet_key, text_file_dictionary):
    account = input(
    "\nFrom which Account would you like to access the password?\n>"
    )

    password_to_de = text_file_dictionary.get(account)

    password_de = encryption_functions.input_to_decrypt(password_to_de, fernet_key)

    print(f"The password is:{password_de}")

# Erases the account and password that is specified by the user.  

def erase_acc_pw_(text_file_dictionary):
    account_to_erase = input("""
\nWhich account and password would you like to erase? Pls put in the
accountname.
>""")
        
    text_file_dictionary.pop(account_to_erase)

    dict_functions.new_dict(text_file_dictionary)


def change_pw_(fernet_key, text_file_dictionary):
    account = input(
    "\nWhat is the Account of which you would like to change the password?:\n>"
    )

    if account in text_file_dictionary:
        password = input("\nTo what should the password be changed?\n>")

        new_password = encryption_functions.input_to_encrypt(password, fernet_key)

        new_pw_dict = {account: new_password}
        text_file_dictionary.update(new_pw_dict)

        dict_functions.new_dict(text_file_dictionary)
        
    else:
        print("\nAcount does not exits.")


# Clears the dictionay and file containing the account password pairs.
def erase_all_pws_(text_file_dictionary):
    sure = input("\nAre you sure you want to erase all passwords:\n>")
    if sure == "yes":

        sure_sure = input("\n\nAre you certain?\n>")

        if sure_sure == "yes":
            text_file_dictionary.clear()

            dict_functions.new_dict(text_file_dictionary)

        else:
            exit()
        
    else:
        exit()
            
# Erases the old master password and sets a new one.

def new_master_pw_():

    change_verification = input("\nWhat is the masterpassword?\n>")

    with open("masterpw.txt") as v:
        master = v.read()

    change_master= encryption_functions.string_to_hash_func(change_verification)

    if change_master == master:
            
        new_master = input(
        "\nWhat should be the new masterpassword be set to?\n>"
        )
        # Calls the new_master_password fucntion with the new master 
        # password as the argument.
        dict_functions.new_master_password(new_master)

    else:
        exit()
    