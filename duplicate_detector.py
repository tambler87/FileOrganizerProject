import os
import hashlib
import shutil

def calculate_hash(file_path, chunk_size=1024):
    """
    Calculates the SHA-256 hash of a file.

    Args:
        file_path (str): Path to the file.
        chunk_size (int): Size of chunks to read the file in bytes.

    Returns:
        str: The SHA-256 hash of the file.
    """
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(chunk_size):
                sha256.update(chunk)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None
    return sha256.hexdigest()

def find_duplicates(directory):
    """
    Finds duplicate files in a directory by comparing their hashes.

    Args:
        directory (str): Path to the directory to scan.

    Returns:
        dict: A dictionary where the key is the hash and the value is a list of file paths.
    """
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return {}

    file_hashes = {}
    duplicates = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)

            if file_hash:
                if file_hash in file_hashes:
                    # Add to duplicates if hash already exists
                    if file_hash not in duplicates:
                        duplicates[file_hash] = [file_hashes[file_hash]]
                    duplicates[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = file_path

    return duplicates

def handle_duplicates(duplicates, action="list", move_to=None):
    """
    Handles duplicate files based on the chosen action.

    Args:
        duplicates (dict): A dictionary of duplicate files.
        action (str): Action to take ('list', 'delete', or 'move').
        move_to (str): Target directory for moving duplicates (if action is 'move').
    """
    if not duplicates:
        print("No duplicates found.")
        return

    print(f"Found {sum(len(paths) - 1 for paths in duplicates.values())} duplicate files.")

    for file_hash, file_paths in duplicates.items():
        print(f"\nDuplicate group (hash: {file_hash}):")
        for path in file_paths:
            print(f" - {path}")

        if action == "delete":
            for duplicate in file_paths[1:]:  # Keep the first file, delete others
                try:
                    os.remove(duplicate)
                    print(f"Deleted: {duplicate}")
                except Exception as e:
                    print(f"Error deleting file '{duplicate}': {e}")

        elif action == "move" and move_to:
            if not os.path.exists(move_to):
                os.makedirs(move_to)
            for duplicate in file_paths[1:]:  # Keep the first file, move others
                try:
                    shutil.move(duplicate, move_to)
                    print(f"Moved: {duplicate} -> {move_to}")
                except Exception as e:
                    print(f"Error moving file '{duplicate}': {e}")

def main():
    """
    Main function to allow repeated actions for duplicate handling.
    """
    while True:
        target_directory = input("\nEnter the directory to scan for duplicates: ")
        action = input("Choose action for duplicates (list/delete/move): ").strip().lower()
        move_to_folder = None

        if action == "move":
            move_to_folder = input("Enter the folder to move duplicates to: ").strip()

        duplicates = find_duplicates(target_directory)
        handle_duplicates(duplicates, action, move_to=move_to_folder)

        # Ask if the user wants to perform another action
        another_action = input("\nDo you want to perform another action? (yes/no): ").strip().lower()
        if another_action != "yes":
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
