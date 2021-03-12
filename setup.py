from sys import exit
import json
import hashlib
from cryptography.fernet import Fernet

def new_master_password(new_master):
    new_master_hash = string_to_hash_func(new_master)

    erase_file_new_content("masterpw.txt", new_master_hash)

def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string

def erase_file_new_content(file_to_change, new_content):
    with open(file_to_change, 'w') as file_to_c:
        file_to_c.write(new_content)

def password_to_encrypt(input_user):
    password_fer = fernet_string_encrypting(input_user, fernet_key)
    password_fer_encoded = password_fer.decode()

    return password_fer_encoded

def fernet_string_encrypting(string_to_encrypt, fernet_key):

    f = Fernet(fernet_key)
    string_to_encrypt_b = string_to_encrypt.encode()
    token = f.encrypt(string_to_encrypt_b)

    return token

def new_dict():
    with open(filename, 'w') as file:
        file.write(json.dumps(text_file_dictionary))


print("""
    Thank you for using pwManager. First we need to set a Masterpassword
    and we need to generate a Fernet key. Fernet is the encryption method
    used for the passwords. 
    DO NOT PROGRESS FURTHER IF YOU ALLREADY DID THE SETUP ONCE!
    """)

progress = input("Do you want to progress furhter?\n yes or no\n>")

if progress == "yes":

    masterpassword = input(""""
                Pls set a masterpassword.\n CAUTION: Do not lose it and store it
                somewhere safe. A usbstick would be good because you also need
                to store your fernet key somewhere safe.
                """)

    new_master_password(masterpassword)

    print(f"You set your masterpassword as: {masterpassword}")

    fernet_key = Fernet.generate_key()



    print(f"""
    Your Fernet key is: {fernet_key}\n Pls store it offline and not on the
    same pc as the passwordmanager itself. Security is compromised otherwise.
    """)

    set_password = input("""
    Do you want to set some accounts and passwords?\nOptions: yes or no.\n>
    """)

    if set_password =="yes":

        text_file_dictionary = {}

        con = True

        while con == True:
            account = input("Pls input the account.\n>")
            password = input("Pls input the password.\n>")

            encrypted_password = password_to_encrypt(password)

            new_pw_dict = {account: encrypted_password}
            text_file_dictionary.update(new_pw_dict)

            con_ = input("Do you want to add more?\n y or n\n>")

            if con_ == "y":
                continue
        
            elif con_ == "n":
                break
            else:
                print("Not a valid option.")
            


    
    if set_password == "no":
        exit()

    else: 
        print("No valid command.\nProgramm will exit now.")
        exit()

else:
    exit()


