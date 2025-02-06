#!/usr/bin/env python3

from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted)

    print(f"File '{file_path}' encrypted successfully.")

def decrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)

    with open(file_path, 'wb') as file:
        file.write(decrypted)

    print(f"File '{file_path}' decrypted successfully.")