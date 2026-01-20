#!/usr/bin/env python3
"""
Validate all POI files for frontend compatibility.
Check:
1. Valid JSON
2. Required fields present
3. Images field (if present) is array of strings, not empty array
4. No object-formatted images
"""

import json
import os
from pathlib import Path

def validate_poi(filename):
    """Validate a single POI file"""
    filepath = os.path.join('pois', filename)
    issues = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check required fields
        required_fields = ['name', 'description', 'category', 'coordinates']
        for field in required_fields:
            if field not in data:
                issues.append(f"Missing required field: {field}")

        # Check coordinates subfields
        if 'coordinates' in data:
            coord_fields = ['latitude', 'longitude']
            for field in coord_fields:
                if field not in data['coordinates']:
                    issues.append(f"Missing coordinate field: {field}")

        # Check images field if present
        if 'images' in data:
            if not isinstance(data['images'], list):
                issues.append("images field is not a list")
            elif len(data['images']) == 0:
                issues.append("images field is empty array (should be absent)")
            else:
                # Check that all items are strings, not objects
                for idx, img in enumerate(data['images']):
                    if not isinstance(img, str):
                        issues.append(f"images[{idx}] is not a string: {type(img).__name__}")

    except json.JSONDecodeError as e:
        issues.append(f"Invalid JSON: {str(e)}")
    except Exception as e:
        issues.append(f"Error: {str(e)}")

    return issues

def main():
    print("Validating all 389 POI files...")
    print("=" * 60)

    pois_dir = Path('pois')
    poi_files = sorted([f.name for f in pois_dir.glob('*.json')])

    total_files = len(poi_files)
    valid_count = 0
    invalid_files = []

    for filename in poi_files:
        issues = validate_poi(filename)
        if issues:
            invalid_files.append((filename, issues))
            print(f"❌ {filename}:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            valid_count += 1

    print("=" * 60)
    print(f"Total POI files: {total_files}")
    print(f"Valid: {valid_count}")
    print(f"Invalid: {len(invalid_files)}")

    if invalid_files:
        print("\nFiles with issues:")
        for filename, issues in invalid_files:
            print(f"  - {filename}: {len(issues)} issue(s)")
        return False
    else:
        print("\n✅ All POI files are valid and frontend-compatible!")
        return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
