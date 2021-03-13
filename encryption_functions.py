import hashlib
from cryptography.fernet import Fernet

def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string

def fernet_string_encrypting(string_to_encrypt, fernet_key):

    f = Fernet(fernet_key)
    string_to_encrypt_b = string_to_encrypt.encode()
    token = f.encrypt(string_to_encrypt_b)

    return token

def fernet_string_decrypting(string_to_decrypt, fernet_key):

    f = Fernet(fernet_key)
    string_to_decrypt_b = string_to_decrypt.encode()
    decrypted_string = f.decrypt(string_to_decrypt_b)

    return decrypted_string

def password_to_decrypt(input_user, fernet_key):
    password_to_decrypt_decrypted = fernet_string_decrypting(input_user, fernet_key)
    password_to_decrypt_decrypted_d = password_to_decrypt_decrypted.decode()

    return password_to_decrypt_decrypted_d

def password_to_encrypt(input_user, fernet_key):
    password_fer = fernet_string_encrypting(input_user, fernet_key)
    password_fer_encoded = password_fer.decode()

    return password_fer_encoded