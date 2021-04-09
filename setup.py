from sys import exit
import json
import dict_functions
import encryption_functions
from cryptography.fernet import Fernet

# Warns the user to not use this file again if he allready did the setup.
print("""
Thank you for using pwManager. First you need to set a Masterpassword
and we need to generate a Fernet key. Fernet is the encryption method
used for the passwords.

DO NOT PROGRESS FURTHER IF YOU ALLREADY DID THE SETUP ONCE!
""")
# Asks if the user wants to progress further.
progress = input("\nDo you want to progress furhter?\nyes or no\n>")

if progress == "yes":
    # Creates the two files pw.txt and masterpw.txt.
    pw_file = open("pw.txt", "w+")
    master_file = open("masterpw.txt", "w+")

    masterpassword = input("""
\nYou now have to set a masterpassword.
CAUTION: Do not lose it and store it somewhere safe. 
An offline device like a usbstick would be a good choice.
The same applies to the fernet key that will be generated for you.

Pls set a masterpassword.
>""")
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
Please store it offline and not on the same pc as the passwordmanager itself. 
Security is at risk otherwise.
""")

    set_password = input("""
Do you want to set some accounts and passwords?
Options: yes or no.
>""")

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
            account = input("\nPls input the account.\n>")
            password = input("\nPls input the password.\n>")
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
            con_ = input("\nDo you want to add more?\nyes or no\n>")

            if con_ == "yes":
                continue
        
            elif con_ == "no":
                break
            else:
                print("\nNot a valid option.")
                break
            
    if set_password == "no":
        exit()

    else: 
        print("\nNo valid command.\nProgramm will exit now.")
        exit()

else:
    exit()


