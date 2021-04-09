import json
import encryption_functions

# Opens the specified textfile and writes the in "text_file_dictionary" stored
# dictionary into it in the json format.
def new_dict(text_file_dictionary):
    with open("pw.txt", 'w') as file:
        file.write(json.dumps(text_file_dictionary, indent = 2))

# Erases all the contents of a file and writes the "new_contnet" into it.
def erase_file_new_content(file_to_change, new_content):
    with open(file_to_change, 'w') as file_to_c:
        file_to_c.write(new_content)

# Runs the entered new_master password through sha256 to create the hash of the
# password and calls the erase_file_new_content function with the file into which
# the hash should be written into and the hash as arguments.
def new_master_password(new_master):
    new_master_hash = encryption_functions.string_to_hash_func(new_master)

    erase_file_new_content("masterpw.txt", new_master_hash)