import random
import math

password = "password123"
letters = ["a","b", "c"]
symbols = ["@", "#", "$"]
numbers = ["1", "2", "3"]
encrypt_path = {}
encpw = []

def encrpyt(x):
    for i in password:
        x = random.randint(0,2)
        y = random.randint(0,len(password))

        z = password.index(i)
        encpw.append(password[z])

        encpw.append(letters[x])
        encrypt_path[letters[x]] = z
        encpw.append(symbols[x])
        encrypt_path[symbols[x]] = z
        encpw.append(numbers[x])
        encrypt_path[numbers[x]] = z

        print(encpw)
        print(encrypt_path)


def decrypt():
    pass

encrpyt(password)