"""
Integrity Checker
"""

import json
import os

from collectors.hash_collector import calculate_hash

def check_integrity(directory, baseline_file):

    print("\nChecking file integrity...\n")

    try:

        with open(baseline_file, "r") as file:

            baseline = json.load(file)

    except:

        print("Baseline database not found.")

        return

    for root, _, files in os.walk(directory):

        for file in files:

            path = os.path.join(root, file)

            current_hash = calculate_hash(path)

            old_hash = baseline.get(path)

            if old_hash is None:

                print(f"[NEW] {path}")

            elif current_hash != old_hash:

                print(f"[MODIFIED] {path}")

            else:

                print(f"[OK] {path}")
