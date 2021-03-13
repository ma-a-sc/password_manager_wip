def new_dict():
    with open(filename, 'w') as file:
        file.write(json.dumps(text_file_dictionary))

def erase_file_new_content(file_to_change, new_content):
    with open(file_to_change, 'w') as file_to_c:
        file_to_c.write(new_content)

def new_master_password(new_master):
    new_master_hash = string_to_hash_func(new_master)

    erase_file_new_content("masterpw.txt", new_master_hash)