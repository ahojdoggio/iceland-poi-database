#!/usr/bin/env python3
"""
Cross-reference potential POIs against current database to find missing ones
"""

import json
import os
from difflib import SequenceMatcher

def normalize_name(name):
    """Normalize POI names for comparison"""
    # Remove common suffixes/prefixes for better matching
    name = name.lower()
    name = name.replace('the ', '')
    name = name.replace('–', '-')
    name = name.replace('—', '-')
    # Remove location descriptors
    for remove in [' - ', ' (', ')']:
        if remove in name:
            name = name.split(remove)[0]
    return name.strip()

def similar(a, b):
    """Check if two strings are similar"""
    return SequenceMatcher(None, normalize_name(a), normalize_name(b)).ratio() > 0.85

def get_current_pois():
    """Get all current POI names from database"""
    pois = []
    pois_dir = 'pois'

    for filename in os.listdir(pois_dir):
        if not filename.endswith('.json'):
            continue

        filepath = os.path.join(pois_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            name = data.get('name', '')
            if name:
                pois.append(name)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return pois

def check_potential_pois():
    """Check potential POIs from knowledge base"""

    # Comprehensive list of potential POIs based on Iceland knowledge
    potential_pois = {
        "Waterfalls": [
            "Glanni", "Hundafoss", "Strompgljúfrafoss", "Gvendarfoss",
            "Sigöldufoss", "Ófærufoss", "Múlagljúfur Canyon Waterfall",
            "Stjórnarfoss", "Klifbrekkufossar", "Folaldafoss",
            "Basaltic Organ Waterfall"
        ],
        "Mountains & Viewpoints": [
            "Stóri-Dímon", "Borgarvirki", "Hafnarfjall",
            "Kirkjufell Summit Trail", "Helgafell (Snæfellsnes)",
            "Helgafell (Þingvellir)", "Öræfajökull", "Hvannadalshnjúkur"
        ],
        "Museums": [
            "Living Art Museum", "Reykjavík City Museum",
            "Museum of Design and Applied Art", "Skógar Folk Museum",
            "Þórbergur Center", "Library of Water",
            "Museum of Icelandic Sorcery & Witchcraft", "Nonsense Museum Ísafjörður",
            "Langabúð Djúpivogur", "Whales of Iceland", "Volcano House",
            "FlyOver Iceland", "Tales from Iceland"
        ],
        "Hot Springs & Pools": [
            "Laugavallalaug", "Grettislaug Reykir", "Kvika Footbath",
            "Lýsuhólslaug", "Húsafell Canyon Baths", "Húsavík Swimming Pool",
            "Hafnarfjörður Pool", "Pollurinn Tálknafjörður"
        ],
        "Churches": [
            "Reyniskirkja", "Strandarkirkja", "Seljavallakirkja",
            "Ingjaldshólskirkja", "Núpsstaður Church"
        ],
        "Historic Sites": [
            "Alþingishúsið", "Höfði House", "Menntaskólinn í Reykjavík",
            "Austurvöllur"
        ],
        "Volcanic Sites": [
            "Eldborg", "Leirhnjúkur", "Valahnúkur", "Þríhnjúkagígur",
            "Rauðhólar", "Skútustaðagígar", "Gunnuhver", "Hveradalir",
            "Hverarönd", "Bjarnarflag", "Dimmuborgir", "Lofthellir",
            "Búri", "Surtshellir"
        ],
        "Beaches": [
            "Krísuvíkurbjarg"
        ],
        "Hiking Trails": [
            "Víknaslóðir", "Kleifarvatn Lake Walk"
        ],
        "Towns & Villages": [
            "Þingeyri", "Hnífsdalur", "Suðureyri", "Reykjahlíð",
            "Eskifjörður", "Reyðarfjörður", "Mjóifjörður",
            "Grenivík", "Laugar", "Varmahlíð", "Hvammstangi",
            "Stokkseyri", "Þorlákshöfn"
        ],
        "Restaurants": [
            "Ōx + Vox", "Skál!", "VOX Restaurant", "Fish Company",
            "Þrír Frakkar", "Langoustine Festival Höfn"
        ],
        "Wildlife": [
            "Ingólfshöfði Puffin Island", "Illugastaðir Seal Colony",
            "Akureyri Whale Watching", "Grundarfjörður Orca Watching"
        ],
        "Glaciers": [
            "Hofsjökull", "Drangajökull", "Skaftafellsjökull",
            "Falljökull", "Katla Ice Cave"
        ],
        "Highland Routes": [
            "Askja Route (F88)", "Holuhraun"
        ],
        "Industrial": [
            "Hellisheiði Power Plant", "Nesjavellir Power Plant",
            "Kárahnjúkar Dam", "Svartsengi Power Station"
        ],
        "Airports": [
            "Reykjavík Domestic Airport", "Húsavík Airport"
        ],
        "Bridges": [
            "Skeiðará Bridge Monument", "Jökulsá á Fjöllum Bridge",
            "Ölfusá Bridge", "Hvalfjörður Tunnel"
        ],
        "Islands": [
            "Drangey"
        ]
    }

    current_pois = get_current_pois()

    truly_missing = {}
    possibly_existing = {}

    for category, poi_list in potential_pois.items():
        missing = []
        maybe_exists = []

        for potential in poi_list:
            # Check if it exists in current database
            found = False
            for current in current_pois:
                if similar(potential, current):
                    maybe_exists.append(f"{potential} (similar to: {current})")
                    found = True
                    break

            if not found:
                missing.append(potential)

        if missing:
            truly_missing[category] = missing
        if maybe_exists:
            possibly_existing[category] = maybe_exists

    return truly_missing, possibly_existing

def main():
    print("Cross-referencing potential POIs against current database...")
    print("=" * 70)

    truly_missing, possibly_existing = check_potential_pois()

    # Count totals
    total_missing = sum(len(v) for v in truly_missing.values())
    total_maybe = sum(len(v) for v in possibly_existing.values())

    print(f"\n📊 SUMMARY")
    print(f"Truly Missing: {total_missing} POIs")
    print(f"Possibly Existing: {total_maybe} POIs")
    print("=" * 70)

    print(f"\n🆕 TRULY MISSING POIs ({total_missing}):\n")
    for category, pois in sorted(truly_missing.items()):
        print(f"\n{category} ({len(pois)}):")
        for poi in sorted(pois):
            print(f"  - {poi}")

    print(f"\n\n❓ POSSIBLY ALREADY IN DATABASE ({total_maybe}):\n")
    for category, pois in sorted(possibly_existing.items()):
        print(f"\n{category} ({len(pois)}):")
        for poi in sorted(pois):
            print(f"  - {poi}")

    # Write to file
    with open('docs/CONFIRMED_MISSING_POIS.md', 'w', encoding='utf-8') as f:
        f.write("# Confirmed Missing POIs\n\n")
        f.write("*Generated: 2026-01-23*\n\n")
        f.write(f"**Total Truly Missing: {total_missing} POIs**\n\n")
        f.write("---\n\n")

        for category, pois in sorted(truly_missing.items()):
            f.write(f"\n## {category} ({len(pois)})\n\n")
            for poi in sorted(pois):
                f.write(f"- [ ] {poi}\n")

        f.write("\n\n---\n\n")
        f.write("## Possibly Already in Database (Need Manual Verification)\n\n")

        for category, pois in sorted(possibly_existing.items()):
            f.write(f"\n### {category} ({len(pois)})\n\n")
            for poi in sorted(pois):
                f.write(f"- {poi}\n")

    print(f"\n\n✅ Results written to: docs/CONFIRMED_MISSING_POIS.md")

if __name__ == '__main__':
    main()
