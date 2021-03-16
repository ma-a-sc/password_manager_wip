import json
import encryption_functions

def new_dict(filename, text_file_dictionary):
    with open(filename, 'w') as file:
        file.write(json.dumps(text_file_dictionary, indent = 2))

def erase_file_new_content(file_to_change, new_content):
    with open(file_to_change, 'w') as file_to_c:
        file_to_c.write(new_content)

def new_master_password(new_master):
    new_master_hash = encryption_functions.string_to_hash_func(new_master)

    erase_file_new_content("masterpw.txt", new_master_hash)