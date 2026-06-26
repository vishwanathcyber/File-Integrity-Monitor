"""
Deleted File Detection
"""

import os

def detect_deleted_files(directory, baseline):

    deleted = []

    for file in baseline:

        if not os.path.exists(file):

            deleted.append(file)

    return deleted
