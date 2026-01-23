#!/usr/bin/env python3
"""
Extract all POI names from the current database
"""

import json
import os

def extract_poi_names():
    """Extract all POI names from the database"""
    poi_names = []

    pois_dir = 'pois'
    for filename in sorted(os.listdir(pois_dir)):
        if not filename.endswith('.json'):
            continue

        filepath = os.path.join(pois_dir, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            name = data.get('name', '')
            if name:
                poi_names.append(name)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return sorted(poi_names)

if __name__ == '__main__':
    names = extract_poi_names()
    print(f"Total POIs in database: {len(names)}\n")
    print("Current POI Names:")
    print("=" * 60)
    for name in names:
        print(f"- {name}")
