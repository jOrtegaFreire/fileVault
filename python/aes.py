import json
from base64 import b64encode,b64decode
from unittest import result
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import hashlib

class encrypted_data:
    """!
    @brief   Helper class to hold encrypted data
    @param   iv, type bytes, ciphers initialization vector.
    @param   ct, type bytes, ciphertext.
    """    
    def __init__(self,iv=None,ct=None):
        self.iv=iv
        self.ct=ct


def generate_key(passphrase):
    """!
    @brief   generates key from passphrase
    @param   passphrase, type string.
    """
    _hash=hashlib.new('sha256')
    _hash.update(passphrase.encode())
    return _hash.hexdigest()

def generate_random_key():pass

def encrypt(data,key):
    """!
    @brief   encrypt data using aes256 and key
    @param   data, data to encrypt
    @param   key, 256bit key
    """
    cipher=AES.new(key,AES.MODE_CBC)
    ct_bytes=cipher.encrypt(pad(data,AES.block_size))
    
    return encrypted_data(iv=cipher.iv,ct=ct_bytes)

def decrypt(data,key):
    """!
    @brief   decrypt data using aes256 and key
    @param   data, type list containing iv and ciphertext to deecrypt
    @param   key, 256bit key
    """
    try:
        cipher=AES.new(key,AES.MODE_CBC,data.iv)
        pt=unpad(cipher.decrypt(data.ct),AES.block_size)
        return pt
    except (ValueError,KeyError):
        print("Key Error")

def password_verify(password,hash):
    _hash=hashlib.new('sha256')
    _hash.update(password.encode())
    return _hash.hexdigest()==hash