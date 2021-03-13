import dict_functions
import encryption_functions

class commands(object):

    def __init__(self):
        pass
    pass

class append(commands):


    def __init__(self, fernet_key, text_file_dictionary):
        self.account = input(
            "What is the Accountname you would like to append:\n> "
        )
        self.password = input(
            "To what account should the password be linked?\n> "
        )
        self.fernet_key = fernet_key

        encrypted_password = encryption_functions.password_to_encrypt(self.password, self.fernet_key)

        new_pw_dict = {self.account: encrypted_password}
        text_file_dictionary.update(new_pw_dict)

        dict_functions.new_dict()

        exit()

class get_pw(commands):

    def __init__(self, fernet_key, text_file_dictionary):
        self.account = input(
            "From which Account would you like to access the password?\n> "
        )

        self.fernet_key = fernet_key

        password_to_de = text_file_dictionary.get(self.account)

        password_de = encryption_functions.password_to_decrypt(password_to_de, self.fernet_key)

        print(password_de)

    
class erase_acc_pw(commands):


    def __init__(self, text_file_dictionary):
        self.account_to_erase = input("""
            Which account and password would you like to erase? Pls put in the
            accountname.\n> 
            """)
        
        account_erase = text_file_dictionary.get(self.account_to_erase)
        
        text_file_dictionary.pop(account_erase)

        dict_functions.new_dict()

class change_pw(commands):

    def __init__(self, fernet_key, text_file_dictionary):
        self.account = input(
            "What is the Accountname you would like to append:\n> "
            )
        
        self.fernet_key = fernet_key

        if self.account in text_file_dictionary:
            password = input(
                "To what should the password be changed?\n> "
            )


            new_password = encryption_functions.password_to_encrypt(password, self.fernet_key)

            new_pw_dict = {self.account: new_password}
            text_file_dictionary.update(new_pw_dict)

            dict_functions.new_dict()
        
        else:
            print("Acount does not exits.")
            exit()

class erase_all_pws(commands):

    def __init__(self, text_file_dictionary):
        self.sure = input("Are you sure you want to erase all passwords:\n> ")
        if self.sure == "yes":

            sure_sure = input("Are you certain?")

            if sure_sure == "yes":
                text_file_dictionary.clear()

                dict_functions.new_dict()

            else:
                exit()
        
        else:
            exit()