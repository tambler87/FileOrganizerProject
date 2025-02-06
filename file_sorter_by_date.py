#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

def organize_by_date(directory, date_type='modification', simulate=False):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if not os.path.isfile(file_path):
            continue

        if date_type == 'creation':
            date = os.path.getctime(file_path)
        else:
            date = os.path.getmtime(file_path)

        folder_name = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        target_folder = os.path.join(directory, folder_name)

        if not os.path.exists(target_folder):
            if not simulate:
                os.makedirs(target_folder)
            print(f"Created folder: {target_folder}")

        if not simulate:
            shutil.move(file_path, os.path.join(target_folder, file))
        print(f"Moved '{file}' to '{target_folder}'")

    print("Date-based organization complete!" if not simulate else "Preview complete!")