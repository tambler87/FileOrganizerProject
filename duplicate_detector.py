#!/usr/bin/env python3

import os
import hashlib

def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    seen = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = hash_file(path)

            if file_hash in seen:
                print(f"Duplicate found: {path} and {seen[file_hash]}")
            else:
                seen[file_hash] = path

    print("Duplicate scan complete.")