#!/usr/bin/env python3

from duplicate_detector import find_duplicates
from file_sorter_by_type import organize_by_type
from file_sorter_by_date import organize_by_date
from file_encryptor import encrypt_file, decrypt_file

def menu():
    while True:
        print("\nFile Organizer Menu:")
        print("1. Organize files by type")
        print("2. Organize files by date")
        print("3. Detect duplicate files")
        print("4. Encrypt a file")
        print("5. Decrypt a file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            directory = input("Enter the directory path: ").strip()
            simulate = input("Simulate changes? (yes/no): ").lower() == "yes"
            organize_by_type(directory, simulate)

        elif choice == "2":
            directory = input("Enter the directory path: ").strip()
            date_type = input("Sort by (creation/modification): ").strip().lower()
            simulate = input("Simulate changes? (yes/no): ").lower() == "yes"
            organize_by_date(directory, date_type, simulate)

        elif choice == "3":
            directory = input("Enter the directory path: ").strip()
            find_duplicates(directory)

        elif choice == "4":
            file_path = input("Enter file path to encrypt: ").strip()
            password = input("Enter password: ").strip()
            encrypt_file(file_path, password)

        elif choice == "5":
            file_path = input("Enter file path to decrypt: ").strip()
            password = input("Enter password: ").strip()
            decrypt_file(file_path, password)

        elif choice == "6":
            print("Exiting File Organizer. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()