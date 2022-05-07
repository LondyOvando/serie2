#LondyOvando 7690-18-193
from email import message
from hashlib import new
from random import random
from ssl import _Cipher
from telnetlib import ENCRYPT
import Crypto

import binascii 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP 
#import ast


random_generator = Crypto.Random.new().read

private_key = RSA.generate(4096, random_generator)
public_key = private_key.publickey()

private_key = private_key.exportKey(format='DER')
public_key = public_key.exportKey(format='DER')

private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')
print(private_key)
print(public_key)

#el inverso muestra de la clave encryptada
private_key = RSA.importKey(binascii.unhexlify(private_key))

public_key = RSA.importKey(binascii.unhexlify(public_key)

message = 'Aqui lo que se necesita descifrar'
message = message.encode()#impresion de mensaje encryptado

Cipher = PKCS1_OAEP.new(public_key)
encrypted message =Cipher.encrypt(message)

print(encrypted_message)

cipher = PKCS1_OAEP.new(private_key)
message =cipher.decrypt(encrypted_message)

print(message)#impresion de mensaje desemcryptado. 