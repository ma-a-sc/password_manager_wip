from sys import argv
from sys import exit

import sys

sys.path.append("Users\Ma_a_sc\Documents\Python\Password_Manager_Development\password_manager_wip")

import json
import hashlib
from cryptography.fernet import Fernet
import pwManager_c
import dict_functions
import encryption_functions


script, filename = argv

verification = input("What is the masterpassword?\n> ")

masterpassword_hash = encryption_functions.string_to_hash_func(verification)

with open("masterpw.txt") as v:
    master = v.read()

if masterpassword_hash == master:
    fernet_key = input("Pls insert decoding key.\n>")

    
    with open(filename, 'r') as m:
        contents = m.read()

    
    text_file_dictionary = json.loads(contents)

    
    command = input("""
        What action would you like to perform?\n
        Actions: append, get pw, erase acc and pw, change pw, erase all pws,
        change masterpassword\n> 
        """)

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

        change_secure2 = encryption_functions.string_to_hash_func(change_verification)

        if change_secure2 == master:
            
            new_master = input(
                "What should be the new masterpassword be set to?\n>"
                )

            dict_functions.new_master_password(new_master)

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