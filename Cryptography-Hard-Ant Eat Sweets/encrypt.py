import base64
import random
from Crypto.Cipher import AES

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message) % 16)
    return message

def encrypt(key, plain):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plain)

flag = open('flag.txt').read().strip()
message = pad(flag)
message = bytes(message, 'utf-8')
key = 'WCTF23#####' + str(random.randrange(10000, 100000))
cipher = encrypt(key.encode(), message)
cipher = base64.b64encode(cipher)
open('enc.txt', 'w').write(cipher.decode('ascii'))
