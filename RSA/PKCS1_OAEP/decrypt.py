#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys

if len(sys.argv) != 3:
    print('usage: decrypt.py encrypted private_key')
    exit(1)

with open(sys.argv[2], "rb") as f:
    key_read = f.read()

with open(sys.argv[1], "rb") as f:
    encrypted = f.read()

private_key = RSA.importKey(key_read)

cipher = PKCS1_OAEP.new(private_key)
decrypted = cipher.decrypt(encrypted)

with open("decrypted.txt", "w") as f:
    f.write(decrypted.decode())
