from sys import exit
import json
import dict_functions
import encryption_functions
from cryptography.fernet import Fernet

# Creates the two files pw.txt and masterpw.txt.
pw_file = open("pw.txt", "w+")
master_file = open("masterpw.txt", "w+")

# Warns the user to not use this file again if he allready did the setup.
print("""
Thank you for using pwManager. First you need to set a Masterpassword
and we need to generate a Fernet key. Fernet is the encryption method
used for the passwords. 
DO NOT PROGRESS FURTHER IF YOU ALLREADY DID THE SETUP ONCE!
""")
# Asks if the user wants to progress further.
progress = input("Do you want to progress furhter?\nyes or no\n>")

if progress == "yes":

    masterpassword = input("""
Pls set a masterpassword.
CAUTION: Do not lose it and store it
somewhere safe. A usbstick would be good because you also need
to store your fernet key somewhere safe.
""")
    # The user is asked to set a masterpassword. Afterwards the new_master_password
    # function is called to create the hash.
    dict_functions.new_master_password(masterpassword)
    print(f"You set your masterpassword as: {masterpassword}")

    # Generates the Fernet key which is needed for the encryption of the 
    # passwords later on.
    fernet_key = Fernet.generate_key()

    fernet_key2 = fernet_key.decode()

    
    print(f"""
Your Fernet key is: {fernet_key2}
Pls store it offline and not on the same pc as the passwordmanager itself. 
Security is compromised otherwise.
""")

    set_password = input("""
Do you want to set some accounts and passwords?
Options: yes or no.
>
""")

    # Opens the pw.txt and writes two brakets into it. This is needed because
    # otherwise json doesnt recognize an dictionary.
    with open("pw.txt", 'w') as w:
        w.write("{}")
    # Reads the pw.txt file and stores the contents of it in "contents".
    with open("pw.txt", 'r') as m:
        contents = m.read()
    # With json we load the contents of pw.txt into a dictionary.
    text_file_dictionary = json.loads(contents)

    if set_password =="yes":

        con = True
        # Created a loop with which the user can enter multiple accounts and 
        # password combinations.
        while con == True:
            account = input("Pls input the account.\n>")
            password = input("Pls input the password.\n>")
            # Calls the function password_to_encrypt which uses Fernet 
            # to encrypt the password given by the user.
            encrypted_password = encryption_functions.input_to_encrypt(password, fernet_key)
            
            # Simple key value pair with the account and the encrypted password
            # given by the user. Then we update the text_file_dictionary with
            # the key value pair.
            new_pw_dict = {account: encrypted_password}
            text_file_dictionary.update(new_pw_dict)
            
            # The function new_dict is called with the updated text_file_dictionary
            # as the argument. The function writes the updated dictionary into
            # the pw.txt file.
            dict_functions.new_dict(text_file_dictionary)

            # Asks the user if he wants to add more and tests the answer.
            con_ = input("Do you want to add more?\nyes or no\n>")

            if con_ == "yes":
                continue
        
            elif con_ == "no":
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


