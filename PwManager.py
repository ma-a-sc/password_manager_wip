from sys import exit
import json
import pwManager_c
import dict_functions
import encryption_functions

# Function that checks which command the user would like to perform using if
# statements. The function will be called again if the user did not want to exit
# after the command was performed.
def user_inputs(fernet_key, text_file_dictionary):
    command = input("""
What action would you like to perform?
Actions: append, get pw, erase acc and pw, change pw, erase all pws,
change masterpassword, exit
>""")

    if command == 'append':
        pwManager_c.append(fernet_key, text_file_dictionary)
        user_inputs(fernet_key, text_file_dictionary)
    
    elif command == 'get pw':
        pwManager_c.get_pw(fernet_key, text_file_dictionary)
        user_inputs(fernet_key, text_file_dictionary)
        
    elif command == 'erase acc and pw':
        pwManager_c.erase_acc_pw(text_file_dictionary)
        user_inputs(fernet_key, text_file_dictionary)

    elif command == 'change pw':
        pwManager_c.change_pw(fernet_key, text_file_dictionary)
        user_inputs(fernet_key, text_file_dictionary)

    elif command == 'erase all pws':
        pwManager_c.erase_all_pws(text_file_dictionary)
        user_inputs(fernet_key, text_file_dictionary)

    elif command == 'change masterpassword':
        pwManager_c.new_master_pw()
        user_inputs(fernet_key, text_file_dictionary)

    elif command == 'exit':
        exit()
        
    else:
        print("I don't know this command.")
        ex = input("Do you want to exit?\nyes or no\n>")
        if ex == "yes":
            exit()
        elif ex == "no":
            user_inputs(fernet_key, text_file_dictionary)
        else:
            print("Invalid, will exit now")
            exit()

def verification():

    attempts_to_log_in = 0 

    if attempts_to_log_in <= 2:
        verification = input("What is the masterpassword?\n> ")
        masterpassword_hash = encryption_functions.string_to_hash_func(verification)

        # Opens the file in which the hash for the current master password is stored 
        # and sets "master" equal to the content.
        with open("masterpw.txt") as v:
            master = v.read()

        # Checks if both of the hashs (user input generated hash, hash from file) are 
        # the same. If that is not the case the programm will exit.
        if masterpassword_hash == master:
            # asks the user for the in the setup.py file generated key.
            fernet_key = input("Pls insert decoding key.\n>")
            # Opens the file where the accounts and encrypted passwords are 
            # stored and loads them into the variable contents.
            with open("pw.txt", 'r') as m:
                contents = m.read()
            # Creates a dictionary using the json function loads with the 
            # variable contents as the argument.
            text_file_dictionary = json.loads(contents)
            
            user_inputs(fernet_key, text_file_dictionary)

        else:
            attempts_to_log_in += 1

    elif attempts_to_log_in > 2:
        print("Failed to log in.")
        exit()

verification()

