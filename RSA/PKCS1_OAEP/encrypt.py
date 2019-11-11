#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys

if len(sys.argv) != 3:
    print('usage: encrypt.py file public_key')
    exit(1)

with open(sys.argv[2],'rb') as f:
    key_read = f.read()

with open(sys.argv[1],'r') as f:
    message = f.read().encode()
  
public_key = RSA.importKey(key_read)  
  
cipher = PKCS1_OAEP.new(public_key)
cipherText = cipher.encrypt(message)  
  
with open('encrypted.txt', 'wb') as f:
    message = f.write(cipherText)


