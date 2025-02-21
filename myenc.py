import random
import math

#creating encyption for passwords entered in Family Reunion Hub code

letters = ["aagfdgff","btb", "csc"]
symbols = ["@#%&^&^&^", "#$#", "$&^"]
numbers = ["1156356463542", "222", "363"]
all = letters + symbols + numbers
encrypt_path = []
encpw = []


def encrypt(pw):
    for i in pw:
        x = random.randint(0,2)
        y = random.randint(0,len(pw))

        z = pw.index(i)
        encpw.append(pw[z])

        encpw.append(letters[x])
        encrypt_path.append(letters[x])
        encpw.append(symbols[x])
        encrypt_path.append(symbols[x])
        encpw.append(numbers[x])
        encrypt_path.append(numbers[x])

    return encpw


def decrypt(p):

    #making a copy of tuple password
    z = p.copy()

    for i in p:
        if i in all:
            z.remove(i)
        else:
            continue
    
    return z