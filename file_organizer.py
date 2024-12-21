import os

def menu():
    while True:
        print("\nFile Organizer - Main Menu")
        print("1. Sort Files by Type")
        print("2. Sort Files by Date")
        print("3. Detect Duplicate Files")
        print("4. Encrypt Files")
        print("5. Decrypt Files")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            from file_sorter_by_type import organize_by_type
            directory = input("Enter the directory to organize: ").strip()
            simulate = input("Enable simulation mode? (yes/no): ").strip().lower() == "yes"
            organize_by_type(directory, simulate=simulate)

        elif choice == "2":
            from file_sorter_by_date import organize_by_date
            directory = input("Enter the directory to organize: ").strip()
            date_type = input("Organize by (creation/modification): ").strip().lower()
            simulate = input("Enable simulation mode? (yes/no): ").strip().lower() == "yes"
            organize_by_date(directory, date_type, simulate=simulate)

        elif choice == "3":
            from duplicate_detector_with_loop import main as duplicate_detector
            duplicate_detector()

        elif choice == "4":
            from file_encryptor import encrypt_file
            file_path = input("Enter the file path to encrypt: ").strip()
            password = input("Enter the password: ").strip()
            encrypt_file(file_path, password)

        elif choice == "5":
            from file_encryptor import decrypt_file
            file_path = input("Enter the file path to decrypt: ").strip()
            password = input("Enter the password: ").strip()
            decrypt_file(file_path, password)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
