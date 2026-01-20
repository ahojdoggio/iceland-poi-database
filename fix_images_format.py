#!/usr/bin/env python3
"""
Fix images format in POI files.
Convert from object arrays [{"source": "...", "url": "..."}]
to string arrays ["url"]
"""

import json
import os

# List of all POI files with object-formatted images
affected_files = [
    'akranes.json', 'akureyri_swimming_pool.json', 'arnarstapi.json', 'blue_lagoon.json',
    'borgarnes.json', 'budakirkja.json', 'christmas_house.json', 'crystal_ice_cave.json',
    'deildartunguhver.json', 'diamond_beach.json', 'djúpalónssandur.json', 'drangsnes_hot_tubs.json',
    'dynjandi.json', 'dyrholaey.json', 'esjan.json', 'exploration_museum.json',
    'eyjafjallajokull.json', 'fagrifoss.json', 'fjadrargljufur_canyon.json', 'fjallsarlon.json',
    'geysir.json', 'gljufrabui.json', 'glymur.json', 'godafoss.json',
    'grettislaug_pool.json', 'grjotagja.json', 'gullfoss.json', 'gvendarlaug.json',
    'hallgrimskirkja.json', 'harpa_concert_hall.json', 'hellnar.json', 'hellulaug.json',
    'hengifoss.json', 'hjorleifshofdi.json', 'hlíðarfjall.json', 'hoffell_hot_tubs.json',
    'hofn.json', 'hofskirkja.json', 'hofsós_pool.json', 'hotel_heydalur_pools.json',
    'hraunfossar_&_barnafossar.json', 'hrísey.json', 'husavik.json', 'hvalfjörður.json',
    'hveragerdi.json', 'húsavík_lighthouse.json', 'húsavík_whale_museum.json', 'húsavík_wooden_church.json',
    'into_the_glacier_tunnel.json', 'jokulsarlon_glacier_lagoon.json', 'kerið.json', 'kirkjufell.json',
    'kirkjufellsfoss.json', 'kleifarvatn.json', 'krafla.json', 'krauma_spa.json',
    'krossneslaug_pool.json', 'kvernufoss.json', 'lake_myvatn.json', 'lake_viti.json',
    'langjokull_glacier.json', 'laufás_museum_and_heritage_site.json', 'laugarvatn_fontana_spa.json', 'lava_centre.json',
    'londrangar.json', 'myrdalsjokull_glacier.json', 'mývatn_nature_baths.json', 'namaskard.json',
    'national_gallery_of_iceland.json', 'national_museum_of_iceland.json', 'old_harbour.json', 'oxararfoss.json',
    'perlan_museum.json', 'pollurinn_hot_tubs.json', 'raudfeldsgja_gorge.json', 'reykholt.json',
    'reykjafjardarlaug_hot_pool.json', 'reykjavik_art_museum.json', 'reykjavík.json', 'reynisdrangar.json',
    'reynisfjara_black_sand_beach.json', 'saga_museum.json', 'saxholl_crater.json', 'secret_lagoon.json',
    'seljalandsfoss.json', 'seltun.json', 'settlement_center.json', 'skaftafell.json',
    'skalholt.json', 'skogafoss.json', 'sky_lagoon.json', 'snaefellsjokull_national_park.json',
    'snæfellsjökull.json', 'solheimajokull_glacier.json', 'solheimasandur_plane_wreck.json', 'stokksnes.json',
    'stykkisholmur.json', 'sun_voyager.json', 'svartifoss.json', 'svinafellsjokull_glacier.json',
    'thingvellir_national_park.json', 'thjorsardalur.json', 'tjornin.json', 'vatnajokull_glacier.json',
    'vatnajokull_national_park.json', 'vestrahorn.json', 'vik.json', 'ytri_tunga.json',
    'þingvellir_national_park.json'
]

def fix_images_format(filename):
    """Convert images from object array to string array"""
    filepath = os.path.join('pois', filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'images' in data and isinstance(data['images'], list) and len(data['images']) > 0:
        # Check if images are objects
        if isinstance(data['images'][0], dict):
            # Extract URLs from objects
            urls = []
            for img in data['images']:
                if isinstance(img, dict) and 'url' in img:
                    urls.append(img['url'])

            # Replace with string array
            data['images'] = urls

            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')

            return True

    return False

def main():
    print("Fixing images format in 111 POI files...")
    print("=" * 60)

    fixed_count = 0
    errors = []

    for filename in affected_files:
        try:
            if fix_images_format(filename):
                fixed_count += 1
                print(f"✅ Fixed: {filename}")
            else:
                print(f"⚠️  Skipped: {filename} (already correct or no images)")
        except Exception as e:
            errors.append(f"{filename}: {str(e)}")
            print(f"❌ Error: {filename} - {str(e)}")

    print("=" * 60)
    print(f"Fixed: {fixed_count} files")

    if errors:
        print(f"Errors: {len(errors)}")
        for error in errors:
            print(f"  - {error}")
    else:
        print("All files processed successfully!")

    return len(errors) == 0

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
