import os

# List of folders or file extensions to ignore
IGNORE_LIST = ["node_modules", "venv", ".git", ".exe", ".dll", ".project-config"]

def is_ignored(path):
    """
    Checks if a file or folder should be ignored.
    
    Args:
        path (str): The path to check.
    
    Returns:
        bool: True if the path should be ignored, False otherwise.
    """
    for ignore_item in IGNORE_LIST:
        if ignore_item in path:
            return True
    return False

def scan_directory(directory):
    """
    Scans a directory and lists all files, excluding ignored paths.
    
    Args:
        directory (str): The path to the directory to scan.
        
    Returns:
        list: A list of file paths.
    """
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return []
    
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d))]
        
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if not is_ignored(file_path):
                files.append(file_path)
    return files

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory to scan: ")
    file_list = scan_directory(directory_path)
    print(f"Found {len(file_list)} files (excluding ignored paths):")
    for file in file_list:
        print(file)
