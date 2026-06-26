"""
File Integrity Monitor

Main application entry point.
"""

from collectors.hash_collector import calculate_hash
from monitors.baseline import create_baseline

def main():

    print("=" * 60)
    print("File Integrity Monitor")
    print("=" * 60)

    directory = "monitored_files"

    create_baseline(directory)

if name == "main":
    main()
