from sys import exit
import json
import dict_functions
import encryption_functions


## ATTTENTION: have to earase the argvs and to set the static files in the code.
## This approach is better because it requieres less from the user and the 
## he/she can do less wrong.

pw_file = open("pw.txt", "w+")

master_file = open("masterpw.txt", "w+")


print("""
    Thank you for using pwManager. First you need to set a Masterpassword
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
    with open("pw.txt", 'w') as w:
        w.write("{}")

    with open("pw.txt", 'r') as m:
        contents = m.read()

    text_file_dictionary = json.loads(contents)

    if set_password =="yes":

        con = True

        while con == True:
            account = input("Pls input the account.\n>")
            password = input("Pls input the password.\n>")

            encrypted_password = password_to_encrypt(password)

            new_pw_dict = {account: encrypted_password}
            text_file_dictionary.update(new_pw_dict)

            new_dict()

            con_ = input("Do you want to add more?\n yes or no\n>")

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


