"""
Baseline Creation
"""

import os

from collectors.hash_collector import calculate_hash

def create_baseline(directory):

    print("\nCreating baseline...\n")

    for root, _, files in os.walk(directory):

        for file in files:

            path = os.path.join(root, file)

            file_hash = calculate_hash(path)

            print(f"{path} -> {file_hash}")
