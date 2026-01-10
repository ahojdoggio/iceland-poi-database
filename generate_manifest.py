#!/usr/bin/env python3
"""
Script to generate a manifest.json file listing all JSON files in the app folder.
This helps the web app discover and load all POI JSON files.
"""

import json
import os
from pathlib import Path

def generate_manifest():
    """Generate manifest.json with list of all JSON files in app folder."""

    script_dir = Path(__file__).parent
    app_dir = script_dir

    # Find all JSON files in app folder (excluding manifest.json and other non-POI files)
    json_files = []
    exclude_files = {'manifest.json', 'package.json', 'tsconfig.json', 'package-lock.json'}

    for file in app_dir.glob("*.json"):
        if file.name not in exclude_files:
            json_files.append(file.name)

    # Scan /pois/ directory for POI files
    pois_dir = script_dir / "pois"
    poi_files = []
    if pois_dir.exists():
        for file in sorted(pois_dir.glob("*.json")):
            poi_files.append(f"pois/{file.name}")

    # Also check database folder
    database_dir = script_dir.parent / "database"
    database_files = []
    if database_dir.exists():
        for file in database_dir.glob("database_*.json"):
            database_files.append(f"../database/{file.name}")

    manifest = {
        "poi_files": sorted(poi_files),
        "app_folder_files": sorted(json_files),
        "database_files": sorted(database_files),
        "total_files": len(poi_files) + len(json_files) + len(database_files)
    }

    # Save manifest
    manifest_file = app_dir / "manifest.json"
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    print(f"Generated manifest.json with {len(poi_files)} POI files, {len(json_files)} app folder files, and {len(database_files)} database files")
    print(f"POI files: {len(poi_files)} files from /pois/ directory")
    return manifest

if __name__ == "__main__":
    generate_manifest()

