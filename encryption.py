from sys import exit
import hashlib
from cryptography.fernet import Fernet

class encryption(object):

    def __init__(self, text_to_encrypt):
        self.text_to_encrypt = text_to_encrypt

key2 = Fernet.generate_key()

print(key2)

def fernet_string_encoding(string_to_encrypt):
    key = input("Pls insert your encryption key.\n>")
    f = Fernet(key)
    string_to_encrypt_b = string_to_encrypt.encode()
    token = f.encrypt(string_to_encrypt_b)
    print(token)
    return token

def fernet_string_decoding(string_to_decrypt):
    key = input("Pls insert your encryption key.\n>")
    f = Fernet(key)
    decrypted_string = f.decrypt(string_to_decrypt)
    print(decrypted_string)
    return decrypted_string
    

well = fernet_string_encoding("ME")
fernet_string_decoding(well)
