#!/usr/bin/env python3

import os
import shutil

def get_file_category(extension):
    categories = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Others': []
    }
    for category, extensions in categories.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_by_type(directory, simulate=False):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        file_path = os.path.join(directory, file)
        extension = os.path.splitext(file)[1]
        category = get_file_category(extension)

        target_folder = os.path.join(directory, category)
        target_path = os.path.join(target_folder, file)

        if not os.path.exists(target_folder):
            if not simulate:
                os.makedirs(target_folder)
            print(f"Created folder: {target_folder}")

        if not simulate:
            shutil.move(file_path, target_path)
        print(f"Moved '{file}' to '{target_folder}'")

    print("Organization complete!" if not simulate else "Preview complete!")