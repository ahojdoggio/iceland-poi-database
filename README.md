# Iceland POI Database

**A comprehensive database of Points of Interest across Iceland**

[![POIs](https://img.shields.io/badge/POIs-479-blue)]()
[![Status](https://img.shields.io/badge/status-active-green)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

---

## Overview

The Iceland POI Database is a curated collection of tourist attractions, natural landmarks, cultural sites, and infrastructure across Iceland. Each POI includes detailed descriptions, GPS coordinates, contact information, and practical visitor details.

### Current Statistics

| Metric | Count |
|--------|-------|
| **Total POIs** | 479 |
| **Waterfalls** | 37 |
| **Museums** | 36 |
| **Geothermal Pools** | 40+ |
| **Towns & Villages** | 54+ |
| **Restaurants** | 29 |
| **Complete Coverage** | All regions of Iceland |

---

## Database Scope

### Included
- **Natural Attractions:** Waterfalls, glaciers, geysers, volcanic sites, canyons, beaches
- **Cultural Sites:** Museums, churches, historical sites
- **Infrastructure:** Airports, bridges, power plants
- **Activities:** Swimming pools, hiking trails, wildlife sites
- **Services:** Restaurants, cafes, breweries
- **Locations:** Towns, villages, cities

### Excluded (Future Work)
- Camping sites and accommodations (179 sites identified for Phase 3)
- Hotels and guesthouses
- Temporary or seasonal facilities

---

## Quick Start

### Data Structure

Each POI is stored as a JSON file in the `pois/` directory:

```json
{
  "name": "Gullfoss",
  "description": "Gullfoss (Golden Falls) is one of Iceland's most iconic waterfalls...",
  "category": "Waterfall",
  "coordinates": {
    "latitude": 64.327105,
    "longitude": -20.122238,
    "altitude": 70.0
  },
  "phone": "+354 486 6500",
  "website": "https://www.south.is/places/gullfoss",
  "opening_hours": "Open 24/7",
  "images": ["https://example.com/image.jpg"]
}
```

### Using the Database

1. **Browse POIs:** Navigate to the `pois/` directory
2. **Access via manifest:** Use `manifest.json` for a complete index
3. **Search by category:** Filter POIs by their category field
4. **Find by region:** POIs include regional information

---

## Documentation

### Essential Guides

📘 **[DATABASE_STATUS.md](docs/DATABASE_STATUS.md)**
- Current database metrics and progress
- Completed work summary
- Pending work breakdown (71 POIs remaining)
- Roadmap and next actions
- **→ Start here for project status**

📗 **[ENRICHMENT_GUIDE.md](docs/ENRICHMENT_GUIDE.md)**
- POI creation standards and methodology
- 14-step enrichment process
- Quality requirements
- Category taxonomy
- **→ Essential for contributors**

---

## Database Phases

### ✅ Phase 0: Original Database (388 POIs)
**Status:** Complete (January 9, 2026)
- All priority levels completed
- 388 fully enriched POIs
- Complete coverage of major attractions

### ✅ Phase 1: Expansion (20 POIs)
**Status:** Complete (January 23, 2026)
- Added 20 high-priority POIs from confirmed missing list
- Museums, waterfalls, industrial sites, hot springs, towns
- Enhanced 2 existing POIs

### ✅ Phase 2: Confirmed Missing POIs (71 POIs)
**Status:** Complete (January 24, 2026)
- Added 71 POIs across all categories
- Waterfalls (7), volcanic sites (10), museums (7), glaciers (5), mountains (7)
- Bridges (4), churches (4), historic sites (3), pools (5), towns (4)
- Restaurants (4), wildlife sites (4), hiking trails (2), highland routes (2), beaches (1), industrial (2)

### 📋 Phase 3: Camping & Accommodations (179 sites)
**Status:** Future work
- Camping sites, mountain huts, hostels, guesthouses
- Requires coordinate research and full enrichment
- Estimated effort: 100-150 hours

---

## Quality Standards

All POIs meet these requirements:

✅ **Required Fields**
- Unique name
- Detailed description (1400-1800 characters)
- Category from established taxonomy
- GPS coordinates (6+ decimal places)
- Phone number (Iceland format)

✅ **Data Integrity**
- No duplicate names
- Accurate coordinates (Iceland bounds: 63-66°N, -13 to -24°W)
- Valid JSON structure
- Proper file naming conventions

See [ENRICHMENT_GUIDE.md](docs/ENRICHMENT_GUIDE.md) for complete standards.

---

## Technical Details

### File Structure

```
iceland-poi-database/
├── README.md                 # This file
├── manifest.json             # POI index (408 entries)
├── pois/                     # 408 POI JSON files
│   ├── gullfoss.json
│   ├── geysir.json
│   └── ...
├── docs/                     # Documentation
│   ├── DATABASE_STATUS.md    # Project status
│   └── ENRICHMENT_GUIDE.md   # Standards guide
└── scripts/                  # Utility scripts
    ├── generate_manifest.py
    ├── find_duplicate_names.py
    └── ...
```

### Available Scripts

- `generate_manifest.py` - Regenerate manifest.json
- `find_duplicate_names.py` - Check for duplicate POI names
- `identify_missing_pois.py` - Compare lists to find missing POIs
- `extract_poi_names.py` - Extract all POI names from database

---

## Contributing

### Adding New POIs

1. Follow the [ENRICHMENT_GUIDE.md](docs/ENRICHMENT_GUIDE.md) standards
2. Create POI JSON file in `pois/` directory
3. Use proper file naming (lowercase, underscores, no special chars)
4. Regenerate manifest: `python3 generate_manifest.py`
5. Validate with: `python3 find_duplicate_names.py`

### Data Requirements

Before submitting a POI:
- ✅ GPS coordinates researched and verified
- ✅ Description written (1400-1800 characters, 3 paragraphs)
- ✅ Category assigned from taxonomy
- ✅ Phone number in correct format (+354 XXXXXXX)
- ✅ No duplicate names

---

## Project Timeline

| Date | Milestone | POIs |
|------|-----------|------|
| Jan 9, 2026 | Original database complete | 388 |
| Jan 16, 2026 | Fixed display bug | 388 |
| Jan 23, 2026 | Phase 1 expansion | +20 (408 total) |
| Jan 24, 2026 | Phase 2: Missing POIs | +71 (479 total) |
| TBD | Phase 3: Camping sites | +179 (658 total) |

**Current:** 479 POIs
**Target:** 658 POIs (when complete)
**Progress:** 73% complete

---

## License

MIT License - See LICENSE file for details

---

## Contact & Support

For questions, issues, or contributions:
- Check [DATABASE_STATUS.md](docs/DATABASE_STATUS.md) for current status
- Review [ENRICHMENT_GUIDE.md](docs/ENRICHMENT_GUIDE.md) for standards
- Submit issues via GitHub Issues

---

**Last Updated:** January 23, 2026
**Maintained by:** Iceland POI Database Team
**Version:** 1.1
