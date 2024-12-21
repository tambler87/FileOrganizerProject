import os
import shutil
from datetime import datetime

def get_file_date(file_path, date_type):
    """
    Retrieves the date of a file based on the specified type (creation or modification).

    Args:
        file_path (str): Path to the file.
        date_type (str): Type of date to use ('creation' or 'modification').

    Returns:
        tuple: A tuple (year, month, day) based on the file's date.
    """
    if date_type == "creation":
        # Get creation time (Windows only, for cross-platform use os.stat instead)
        timestamp = os.path.getctime(file_path)
    else:
        # Get modification time
        timestamp = os.path.getmtime(file_path)
    
    date = datetime.fromtimestamp(timestamp)
    return date.year, date.strftime('%B'), date.day

def organize_by_date(directory, date_type="modification", simulate=False):
    """
    Organizes files in the given directory by date (Year/Month/Day).

    Args:
        directory (str): Path to the directory to organize.
        date_type (str): Type of date to organize by ('creation' or 'modification').
        simulate (bool): If True, only preview changes without moving files.
    """
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Scan for files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print(f"No files found in '{directory}'.")
        return

    print(f"Found {len(files)} files in '{directory}'.")
    for file in files:
        file_path = os.path.join(directory, file)
        
        try:
            year, month, day = get_file_date(file_path, date_type)
            target_folder = os.path.join(directory, str(year), month, str(day))
        except Exception as e:
            print(f"Error processing '{file}': {e}")
            target_folder = os.path.join(directory, "Unknown")

        # Create the folder hierarchy if it doesn't exist
        if not os.path.exists(target_folder):
            if not simulate:
                os.makedirs(target_folder)
            print(f"Created folder: {target_folder}")

        # Move the file
        target_path = os.path.join(target_folder, file)
        if not simulate:
            shutil.move(file_path, target_path)
        print(f"Moved '{file}' to '{target_folder}'")

    print("Organization complete!" if not simulate else "Preview complete!")

# Example usage
if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    date_type = input("Organize by (creation/modification): ").strip().lower()
    simulate_mode = input("Enable simulation mode? (yes/no): ").strip().lower() == "yes"

    organize_by_date(target_directory, date_type, simulate=simulate_mode)
