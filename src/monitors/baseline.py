"""
Baseline Creation
"""

import json
import os

from collectors.hash_collector import calculate_hash

def create_baseline(directory):

    baseline = {}

    for root, _, files in os.walk(directory):

        for file in files:

            path = os.path.join(root, file)

            baseline[path] = calculate_hash(path)

    with open("src/database/baseline.json","w") as file:

        json.dump(baseline,file,indent=4)

    print("Baseline created successfully.")
