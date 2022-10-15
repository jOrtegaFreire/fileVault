# fileVault

# Requirements

* pip install Pillow  
* pip install pycryptodome

# Description

Simple file manager where you can store files and encript them using AES CBC.
It allows to add files, encrypt them to store them and decrypt them to a temporary
folder, which will get clean on exit the application.  
It also allow to change the encryption key, which will decrypt all the files stored on
the vault an reencrypt them using the new key, you can import files from a differnt vault
and use the key to decrypt the content and reencrypt with your own key.  
Ideal to have on a usb stick as an encrpted vault with the app being portable.
