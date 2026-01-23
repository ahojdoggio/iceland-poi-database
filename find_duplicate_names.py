#!/usr/bin/env python3
"""
Find POI files with duplicate names
"""

import json
import os
from collections import defaultdict

def find_duplicate_names():
    """Find all POI files that have duplicate name values"""
    names_to_files = defaultdict(list)

    pois_dir = 'pois'
    for filename in sorted(os.listdir(pois_dir)):
        if not filename.endswith('.json'):
            continue

        filepath = os.path.join(pois_dir, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            name = data.get('name', '')
            names_to_files[name].append(filename)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    # Find duplicates
    duplicates = {name: files for name, files in names_to_files.items() if len(files) > 1}

    if duplicates:
        print(f"Found {len(duplicates)} duplicate name(s):")
        print("=" * 60)
        for name, files in duplicates.items():
            print(f"\nName: '{name}'")
            print(f"Files ({len(files)}):")
            for f in files:
                print(f"  - {f}")
    else:
        print("No duplicate names found!")

    return duplicates

if __name__ == '__main__':
    find_duplicate_names()
