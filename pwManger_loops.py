from sys import exit
import json
import pwManager_c
import dict_functions
import encryption_functions

def user_inputs():
    command = input("""
    What action would you like to perform?\n
    Actions: append, get pw, erase acc and pw, change pw, erase all pws,
    change masterpassword, exit\n> 
    """)

    if command == 'append':
        pwManager_c.append(fernet_key, text_file_dictionary)
        user_inputs()
    
    elif command == 'get pw':
        pwManager_c.get_pw(fernet_key, text_file_dictionary)
        user_inputs()
        
    elif command == 'erase acc and pw':
        pwManager_c.erase_acc_pw(text_file_dictionary)
        user_inputs()

    elif command == 'change pw':
        pwManager_c.change_pw(fernet_key, text_file_dictionary)
        user_inputs()

    elif command == 'erase all pws':
        pwManager_c.erase_all_pws(text_file_dictionary)
        user_inputs()

    elif command == 'change masterpassword':
        pwManager_c.new_master_pw()
        user_inputs()

    elif command == 'exit':
        exit()
        
    else:
        print("I don't know this command.")
        ex = input("Do you want to exit?\nyes or no\n>")
        if ex == "yes":
            exit()
        elif ex == "no":
            user_inputs()
        else:
            print("Invalid, will exit now")
            exit()


verification = input("What is the masterpassword?\n> ")

masterpassword_hash = encryption_functions.string_to_hash_func(verification)

with open("masterpw.txt") as v:
    master = v.read()

if masterpassword_hash == master:
    fernet_key = input("Pls insert decoding key.\n>")

    with open(file_pw, 'r') as m:
        contents = m.read()

    text_file_dictionary = json.loads(contents)

    user_inputs()

else:
    print("Failed to log in.")
    exit()