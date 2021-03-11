from sys import exit
import hashlib

class encryption(object):

    def __init__(self, text_to_encrypt):
        self.text_to_encrypt = text_to_encrypt


verification = input("What is the masterpassword?\n> ")

verification_d = verification.encode()

# need to hash the verification process
secure = hashlib.sha256()
secure.update(verification_d)
secure2 = secure.hexdigest()


with open("masterpw.txt") as v:
    master = v.read()
    print(master)

master.decode()
