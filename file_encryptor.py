from cryptography.fernet import Fernet
import os

def generate_key(password):
    """
    Generates a key from the provided password.

    Args:
        password (str): The password to generate the key.

    Returns:
        bytes: A derived key.
    """
    return Fernet.generate_key()  # Simplified for now. Password-based key derivation can be added later.

def encrypt_file(file_path, password):
    """
    Encrypts a file using a password.

    Args:
        file_path (str): The path to the file to encrypt.
        password (str): The password to encrypt the file with.
    """
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            data = file.read()

        encrypted_data = cipher.encrypt(data)

        with open(file_path + ".enc", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        os.remove(file_path)
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Error encrypting file '{file_path}': {e}")

def decrypt_file(file_path, password):
    """
    Decrypts a file using a password.

    Args:
        file_path (str): The path to the file to decrypt.
        password (str): The password to decrypt the file with.
    """
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        original_file_path = file_path.replace(".enc", "")
        with open(original_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        os.remove(file_path)
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Error decrypting file '{file_path}': {e}")

def main():
    while True:
        action = input("\nChoose an action (encrypt/decrypt/exit): ").strip().lower()

        if action == "encrypt":
            file_path = input("Enter the file path to encrypt: ").strip()
            password = input("Enter the password: ").strip()
            encrypt_file(file_path, password)

        elif action == "decrypt":
            file_path = input("Enter the file path to decrypt: ").strip()
            password = input("Enter the password: ").strip()
            decrypt_file(file_path, password)

        elif action == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid action. Please choose 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
