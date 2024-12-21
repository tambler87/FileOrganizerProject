import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def get_file_category(extension):
    """Returns the category of a file based on its extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"  # Default category for unknown file types

def organize_by_type(directory, simulate=False):
    """
    Organizes files in the given directory by their type.

    Args:
        directory (str): Path to the directory to organize.
        simulate (bool): If True, only preview changes without moving files.
    """
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Scan the directory for files
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print(f"No files found in '{directory}'.")
        return

    print(f"Found {len(files)} files in '{directory}'.")
    for file in files:
        file_path = os.path.join(directory, file)
        file_extension = os.path.splitext(file)[1]
        category = get_file_category(file_extension)

        # Target folder for the file
        target_folder = os.path.join(directory, category)
        target_path = os.path.join(target_folder, file)

        # Create the folder if it doesn't exist
        if not os.path.exists(target_folder):
            if not simulate:
                os.makedirs(target_folder)
            print(f"Created folder: {target_folder}")

        # Move the file
        if not simulate:
            shutil.move(file_path, target_path)
        print(f"Moved '{file}' to '{target_folder}'")

    print("Organization complete!" if not simulate else "Preview complete!")

# Example usage
if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    simulate_mode = input("Enable simulation mode? (yes/no): ").strip().lower() == "yes"
    organize_by_type(target_directory, simulate=simulate_mode)
