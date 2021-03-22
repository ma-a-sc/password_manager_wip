import dict_functions
import encryption_functions

# dummy class makes it easier to identify the other classes as commands.
class commands(object):

    def __init__(self):
        pass
    pass

# Adds a new key value pair to the dictionary after encrypting the password
# input from the user. Writes the new pair into the pw.txt file.
class append(commands):


    def __init__(self, fernet_key, text_file_dictionary):
        self.account = input(
        "What is the Accountname you would like to append:\n>"
        )
        self.password = input(
        "To what account should the password be linked?\n>"
        )
        self.fernet_key = fernet_key

        encrypted_password = encryption_functions.input_to_encrypt(self.password, self.fernet_key)

        new_pw_dict = {self.account: encrypted_password}
        text_file_dictionary.update(new_pw_dict)

        dict_functions.new_dict(text_file_dictionary)


# Searches the dictionary for a key and decrypts the value. Prints out the value.
class get_pw(commands):

    def __init__(self, fernet_key, text_file_dictionary):
        self.account = input(
        "From which Account would you like to access the password?\n>"
        )

        self.fernet_key = fernet_key

        password_to_de = text_file_dictionary.get(self.account)

        password_de = encryption_functions.input_to_decrypt(password_to_de, self.fernet_key)

        print(f"The password is:{password_de}")

# Erases the account and password that is specified by the user.  
class erase_acc_pw(commands):


    def __init__(self, text_file_dictionary):
        self.account_to_erase = input("""
Which account and password would you like to erase? Pls put in the
accountname.
>""")
        
        text_file_dictionary.pop(self.account_to_erase)

        dict_functions.new_dict(text_file_dictionary)

# Changes the password for an account that is defined by the user. I still have
# to add catches.
class change_pw(commands):

    def __init__(self, fernet_key, text_file_dictionary):
        self.account = input(
        "What is the Account of which you would like to change the password?:\n>"
        )
        
        self.fernet_key = fernet_key

        if self.account in text_file_dictionary:
            password = input("To what should the password be changed?\n>")

            new_password = encryption_functions.input_to_encrypt(password, self.fernet_key)

            new_pw_dict = {self.account: new_password}
            text_file_dictionary.update(new_pw_dict)

            dict_functions.new_dict(text_file_dictionary)
        
        else:
            print("Acount does not exits.")


# Clears the dictionay and file containing the account password pairs.
class erase_all_pws(commands):

    def __init__(self, text_file_dictionary):
        self.sure = input("Are you sure you want to erase all passwords:\n>")
        if self.sure == "yes":

            sure_sure = input("Are you certain?")

            if sure_sure == "yes":
                text_file_dictionary.clear()

                dict_functions.new_dict(text_file_dictionary)

            else:
                exit()
        
        else:
            exit()
            
# Erases the old master password and sets a new one.
class new_master_pw(commands):

    def __init__(self):

        self.change_verification = input("What is the masterpassword?\n>")

        with open("masterpw.txt") as v:
            master = v.read()

        change_master= encryption_functions.string_to_hash_func(self.change_verification)

        if change_master == master:
            
            new_master = input(
            "What should be the new masterpassword be set to?\n>"
            )
            # Calls the new_master_password fucntion with the new master 
            # password as the argument.
            dict_functions.new_master_password(new_master)

        else:
            exit()
    