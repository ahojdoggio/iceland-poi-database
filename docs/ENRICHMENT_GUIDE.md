# POI Enrichment Guide
**Complete Guide for Enriching Iceland POI Database**

---

## 📚 Table of Contents

1. [Quick Start](#quick-start)
2. [14-Step Enrichment Process](#14-step-enrichment-process)
3. [Category Taxonomy Reference](#category-taxonomy-reference)
4. [Data Sources & Search Strategy](#data-sources--search-strategy)
5. [Writing Guidelines](#writing-guidelines)
6. [GPS Coordinate Verification](#gps-coordinate-verification)
7. [Image Sourcing](#image-sourcing)
8. [Quality Checklist](#quality-checklist)
9. [Examples by POI Type](#examples-by-poi-type)
10. [Common Pitfalls](#common-pitfalls)
11. [Time Estimates & Tools](#time-estimates--tools)

---

## Quick Start

**Time per POI:** 12-18 minutes average  
**Process:** 14 simple steps  
**Output:** JSON file in `/island/pois/` directory

**Before you start:**
1. Open this guide
2. Open WORK_CHECKLIST.md to pick a POI
3. Have browser tabs ready: Google Search, Google Maps, Wikimedia Commons

**The 14-Step Process (Summary):**
1. Choose POI → 2. Web search overview → 3. Find GPS coordinates → 4. Get address →  
5. Write description → 6. Assign category → 7. Find website/phone → 8. Research hours →  
9. Source images → 10. Add ratings → 11. Safety warnings → 12. Create JSON →  
13. Save file → 14. Quality check ✓

---

## 14-Step Enrichment Process

### STEP 1: Choose Your POI

**From WORK_CHECKLIST.md**, select a POI to enrich. Follow priorities:
- **Priority 1:** Top 50 attractions (Jökulsárlón, Gullfoss, Blue Lagoon)
- **Priority 2:** Golden Circle & major routes (50 POIs)
- **Priority 3:** Regional capitals & towns (35 POIs)
- **Priority 4:** Specialized sites - pools, restaurants, museums (258 POIs)

**Example:** Let's enrich "Jökulsárlón Glacier Lagoon"

---

### STEP 2: Initial Web Search for Overview

**Search query format:**
```
[POI name] Iceland description location coordinates
```

**Example:**
```
Jökulsárlón glacier lagoon Iceland description GPS coordinates location details
```

**Target sites to check:**
- Guide to Iceland (guidetoiceland.is) - most comprehensive
- Visit Iceland (visiticeland.com) - official tourism
- Regional tourism sites (south.is, northiceland.is, west.is, east.is)
- Wikipedia - historical/geological context
- National park websites if applicable

**Extract from first 3-5 results:**
- Overview of what it is
- Key statistics (size, height, depth, etc.)
- Historical or geological formation
- Why it's famous/unique
- Basic location context

---

### STEP 3: Search for Exact GPS Coordinates

**Search query:**
```
[POI name] GPS coordinates exact latitude longitude
```

**Requirements:**
- Decimal format (e.g., 64.078400, -16.230600)
- Minimum 6 decimal places
- Verify from 2-3 sources

**Iceland coordinate ranges:**
- Latitude: 63.0° to 66.5° N
- Longitude: -13.5° to -24.5° W (negative for West)

**Coordinate sources:**
- latitude.to
- gps-coordinates.net  
- Wikipedia infoboxes
- Official attraction websites
- Google Maps (right-click → "What's here?")

**Verification:**
1. Find from 3 sources
2. Compare and ensure consistency
3. Check on Google Maps satellite view
4. Confirm it's in correct location visually

---

### STEP 4: Research Address & Location Details

**Find:**
- Complete postal address with postal code
- Nearest town/village name
- Distance from Reykjavík or Akureyri
- Route/road number (Route 1, Road 862, etc.)
- Region of Iceland

**Example format:**
```
Address: Route 1, 781 Höfn, Iceland
Location: Southeast Iceland, Vatnajökull National Park
Access: 378km from Reykjavík, directly off Ring Road
```

---

### STEP 5: Write Description (100-300 words)

**Three-paragraph structure:**

**Paragraph 1 (50-80 words) - WHAT IT IS:**
- Name and type of attraction
- Key physical statistics (height, width, depth, area)
- Defining characteristics
- Location context (region, nearest town)

**Paragraph 2 (50-100 words) - WHY IT'S SPECIAL:**
- Formation history (geological/historical)
- Unique features that make it stand out
- Cultural or historical significance
- Superlatives (biggest, only, oldest, etc.)

**Paragraph 3 (50-80 words) - VISITOR EXPERIENCE:**
- What visitors can see and do
- Best viewing points or activities
- Seasonal considerations
- Notable features to look for
- Cultural references (films, legends) if relevant

**Writing rules:**
✅ Start with most important facts  
✅ Use specific numbers and measurements  
✅ Include vivid, concrete details  
✅ Explain geological/historical context  
✅ Mention practical visitor info  

❌ No generic adjectives alone ("beautiful", "amazing")  
❌ No promotional language ("must-see", "don't miss")  
❌ No personal opinions ("you'll love")  
❌ Don't repeat POI name excessively  

**Example opening (Jökulsárlón):**
```
Jökulsárlón is Iceland's most famous glacier lagoon and deepest lake, 
reaching over 284 meters in depth. Located in Vatnajökull National Park 
in southeast Iceland, this stunning glacial lake formed around 1935 when 
Breiðamerkurjökull glacier began retreating from the Atlantic Ocean. The 
lagoon has quadrupled in size since the 1970s and now spans approximately 
25 square kilometers. Massive icebergs, some over 1,000 years old, calve 
from the glacier and drift through the crystal-clear waters...
```

---

### STEP 6: Determine Category

**Choose from Category Taxonomy (see full list below).**

**Main category groups:**
- Natural Attractions (Waterfalls, Glaciers, Lagoons, Beaches, Geothermal)
- Cultural & Historical (Museums, Churches, Heritage Sites)
- Wellness & Recreation (Spas, Swimming Pools)
- Urban & Town POIs (Cities, Towns, Landmarks)
- Food & Drink (Restaurants, Cafés, Breweries)
- Wildlife & Nature Viewing (Whale watching, Puffin colonies)
- National Parks
- Infrastructure (Airports, Lighthouses)

**Be specific:**
- "Glacier Lagoon" not just "Lagoon"
- "Black Sand Beach" not just "Beach"  
- "Geothermal Spa" not just "Spa"
- "Waterfall" is acceptable (don't over-complicate)

**See full taxonomy below** for all 40+ categories.

---

### STEP 7: Find Website & Phone

**Website priority:**
1. Official attraction website (e.g., bluelagoon.com)
2. Regional tourism site (e.g., south.is/en/place/...)
3. National park site (vatnajokulsthjodgardur.is)
4. Guide to Iceland page (last resort)

**Phone format:**
- Iceland country code: +354
- Format: +354 XXX XXXX
- Set to `null` if not publicly available

**Test the website** - make sure URL works before adding.

---

### STEP 8: Research Opening Hours

**Format varies by POI type:**

**Natural sites (waterfalls, beaches):**
```json
"opening_hours": {
  "site": "Accessible 24/7 year-round",
  "parking": "Free parking available" or "800 ISK daily fee",
  "facilities": "Visitor center 09:00-17:00 (summer only)"
}
```

**Managed sites (spas, museums, churches):**
```json
"opening_hours": {
  "summer": "Daily 09:00-20:00 (May-September)",
  "winter": "Daily 10:00-17:00 (October-April)",
  "admission": "Adults 2000 ISK, Children 7-16 years 1000 ISK",
  "notes": "Last entry 1 hour before closing"
}
```

**Roads/seasonal access:**
```json
"opening_hours": {
  "access": "Route 862 (paved) open year-round",
  "summer_only": "Route 864 (gravel) June-September only, 4WD recommended",
  "winter_closure": "Highland roads F-roads closed October-June"
}
```

**Include:** Seasonal variations, parking fees, special requirements

---

### STEP 9: Source Images

**Preferred sources (in order):**

**1. Wikimedia Commons** (copyright-free)
- Go to: commons.wikimedia.org
- Search: "[POI name] Iceland"
- Check license: public domain or free license
- Copy full URL from image page

**2. Official tourism sites:**
- visiticeland.com
- Regional boards: south.is, northiceland.is, west.is, east.is, westfjords.is
- Official attraction websites
- National park sites

**Document format:**
```json
"images": [
  {
    "source": "Wikimedia Commons",
    "url": "https://commons.wikimedia.org/wiki/File:Jokulsarlon.jpg"
  },
  {
    "source": "Visit South Iceland",
    "url": "https://www.south.is/en/place/jokulsarlon"
  }
]
```

**DO NOT USE:**
- Instagram or social media photos
- Personal photography sites
- Stock photo sites (Shutterstock, Getty)
- Sites with unclear copyright

---

### STEP 10: Add Ratings & Review Counts

**Estimate from Google Maps/TripAdvisor:**

**Rating ranges by tier:**
- Major attractions (Jökulsárlón, Gullfoss): 4.7-4.9, 20,000-40,000 reviews
- Popular sites (Goðafoss, Skógafoss): 4.6-4.8, 8,000-20,000 reviews
- Regional attractions: 4.4-4.7, 2,000-8,000 reviews
- Local sites (pools, cafés): 4.2-4.6, 100-2,000 reviews

**Set to `null` if:**
- Very new attraction
- No public ratings available
- Too specialized/niche

---

### STEP 11: Add Safety Warnings (If Critical)

**Include prominent warnings for dangerous sites:**

**Dangerous beaches (Reynisfjara):**
```
"CRITICAL SAFETY WARNING: Extremely dangerous due to unpredictable sneaker 
waves. Never turn your back on ocean, stay far from water's edge. 5 deaths 
since 2007. Swimming strictly prohibited."
```

**Winter hazards:**
```
"Winter access may be closed due to ice hazards and falling icicles. Path 
behind waterfall accessible May-September only."
```

**Highland F-roads:**
```
"4WD vehicle required. Road open June-September only. River crossings required. 
No services available. Emergency beacon recommended."
```

**When in doubt, include warnings** - better safe than sorry.

---

### STEP 12: Create JSON File

**File naming convention:**
- All lowercase
- Replace spaces with underscores
- Replace Icelandic characters: þ→th, ð→d, ó→o, á→a, ö→o, æ→ae
- Add .json extension

**Examples:**
- "Jökulsárlón Glacier Lagoon" → `jokulsarlon_glacier_lagoon.json`
- "Þingvellir National Park" → `thingvellir_national_park.json`
- "Goðafoss" → `godafoss.json`
- "Mývatn Nature Baths" → `myvatn_nature_baths.json`
- "Dyrhólaey" → `dyrholaey.json`

**JSON structure:**
```json
{
  "name": "Official English Name",
  "description": "100-300 words following three-paragraph structure",
  "address": "Complete address with postal code",
  "coordinates": {
    "longitude": -16.230600,
    "latitude": 64.078400,
    "altitude": 0.0
  },
  "rating": 4.8,
  "reviews_count": 28000,
  "category": "Specific Category",
  "website": "https://official-site.com",
  "phone": "+354 478 2222",
  "images": [
    {
      "source": "Wikimedia Commons",
      "url": "https://commons.wikimedia.org/wiki/File:Name.jpg"
    }
  ],
  "opening_hours": {
    "key": "value"
  }
}
```

---

### STEP 13: Save to Output Directory

**Location:** `/Users/shadowofcervobyl/Downloads/island/pois/[filename].json`

**Verify:**
- File saved successfully
- Filename follows naming convention
- JSON is valid (no syntax errors)
- Check file size (should be 1-3 KB typically)

---

### STEP 14: Quality Check

**Run through this checklist before marking complete:**

**✅ Basic Information:**
- [ ] Name is official English name, correctly spelled
- [ ] Category matches approved taxonomy
- [ ] Description is 100-300 words
- [ ] Description follows 3-paragraph structure
- [ ] Specific numbers and measurements included

**✅ Location Data:**
- [ ] GPS coordinates have 6+ decimal places
- [ ] Coordinates verified from 2+ sources
- [ ] Latitude between 63-66° N
- [ ] Longitude between -13 to -24° W (negative)
- [ ] Address includes postal code
- [ ] Address is complete and accurate

**✅ Contact & Hours:**
- [ ] Website URL tested and working
- [ ] Phone in +354 format or null
- [ ] Opening hours include seasonal variations
- [ ] Parking fees mentioned if applicable

**✅ Images:**
- [ ] At least 1 image source documented
- [ ] Wikimedia Commons used if available
- [ ] Copyright-compliant sources only

**✅ Safety & Practical:**
- [ ] Critical safety warnings included if needed
- [ ] Access information clear (roads, closures)
- [ ] Special requirements noted (4WD, permits)

**✅ JSON Format:**
- [ ] File named correctly (lowercase, underscores)
- [ ] JSON is valid (no syntax errors)
- [ ] All required fields present
- [ ] Null used appropriately (not empty strings)

**✅ Final Review:**
- [ ] Read description aloud - does it flow?
- [ ] Would a tourist find this useful?
- [ ] No typos or grammatical errors?
- [ ] Information current (2024-2026)?

---

## Category Taxonomy Reference

### Natural Attractions (~180 POIs)

#### Water Features
- **Waterfall** - Gullfoss, Seljalandsfoss, Skógafoss, Dettifoss, Goðafoss, etc.
- **Glacier Lagoon** - Jökulsárlón, Fjallsárlón
- **Lake** - Mývatn, Kleifarvatn, Þingvallavatn
- **Geothermal Area** - Geysir, Námaskarð/Hverir, Seltún, Gunnuhver
- **Hot Spring** - Landmannalaugar, Reykjadalur, natural hot pools
- **Fjord** - Hvalfjörður, various Westfjords locations

#### Land Features
- **Glacier** - Vatnajökull, Langjökull, Mýrdalsjökull, Snæfellsjökull
- **Ice Cave** - Crystal Ice Cave, Into the Glacier tunnel
- **Volcano** - Hekla, Askja, Krafla, Fagradalsfjall, Eyjafjallajökull
- **Crater** - Kerið, Hverfjall/Hverfell, Saxhóll, Víti
- **Black Sand Beach** - Reynisfjara, Diamond Beach, Djúpalónssandur, Stokksnes
- **Beach** - Rauðisandur, Breiðavík, Ytri-Tunga (seal beach), Nauthólsvík
- **Canyon** - Fjaðrárgljúfur, Ásbyrgi, Stuðlagil, Jökulsárgljúfur
- **Gorge** - Rauðfeldsgjá, Kolugljúfur
- **Lava Field** - Eldhraun, Dimmuborgir, Berserkjahraun, Eldhraun
- **Lava Cave** - Vatnshellir, Raufarhólshellir, Leiðarendi, Víðgelmir
- **Mountain** - Kirkjufell, Vestrahorn, Esjan, Herðubreið
- **Cliff/Promontory** - Dyrhólaey, Látrabjarg, Reynisdrangar, Londrangar
- **Highland Area** - Landmannalaugar, Þórsmörk, Kerlingarfjöll, Askja region

### Cultural & Historical Sites (~70 POIs)

#### Religious & Heritage
- **Church** - Hallgrímskirkja, Akureyrarkirkja, Búðakirkja, Víðimýrarkirkja
- **Turf Church** - Hofskirkja, Grafarkirkja
- **Heritage Site** - Þjóðveldisbærinn Stöng, Eiríksstaðir, turf farms
- **Historic Building** - Bessastaðir (President's Residence), old trading posts
- **UNESCO Site** - Þingvellir, Surtsey

#### Museums & Culture
- **National Museum** - National Museum of Iceland, regional museums
- **Art Gallery** - National Gallery, Reykjavík Art Museum
- **Specialty Museum** - Whale Museum, Saga Museum, Phallological Museum, Punk Museum
- **Heritage Museum** - Settlement Exhibition, Herring Era Museum
- **Open Air Museum** - Árbær, Glaumbær, Laufás

### Wellness & Recreation (~60 POIs)

- **Geothermal Spa** - Blue Lagoon, Sky Lagoon, Mývatn Nature Baths, Krauma
- **Natural Hot Pool** - Secret Lagoon, Seljavallalaug, Grettislaug, Gvendarlaug
- **Swimming Pool** - Laugardalslaug, municipal pools in all towns
- **Seaside Geothermal Bath** - Nauthólsvík, Drangsnes, Krossneslaug

### Urban & Town POIs (~50 POIs)

- **City** - Reykjavík (as overall entry)
- **Town** - Akureyri, Ísafjörður, Höfn, Egilsstaðir, Húsavík, Selfoss
- **Village** - Vík, Stykkishólmur, Seyðisfjörður, Siglufjörður
- **Landmark** - Harpa, Perlan, Sun Voyager, Old Harbour Reykjavík
- **Neighborhood** - Downtown Reykjavík, Old Town areas
- **Park** - Reykjavík Botanical Garden, city parks

### Food & Drink (~35 POIs)

- **Restaurant** - Dill, Grillmarkaðurinn, Fish Company, notable dining
- **Café** - Reykjavík Roasters, Sandholt, Café Loki, local favorites
- **Brewery** - Ölverk, Borg Brugghús, Kaldi
- **Bar** - Notable venues in Reykjavík and regional towns
- **Hot Dog Stand** - Bæjarins Beztu (famous Reykjavík stand)

### Wildlife & Nature Viewing (~30 POIs)

- **Whale Watching** - Húsavík, Reykjavík Old Harbour locations
- **Puffin Colony** - Látrabjarg, Dyrhólaey, Borgarfjörður Eystri
- **Seal Watching** - Vatnsnes, Ytri-Tunga, Hvammstangi
- **Bird Watching Site** - Various cliff colonies, nature reserves
- **Botanical Garden** - Akureyri, Reykjavík

### National Parks & Protected Areas (~20 POIs)

- **National Park** - Þingvellir, Vatnajökull, Snæfellsjökull
- **Nature Reserve** - Hornstrandir, protected wilderness areas
- **Protected Area** - Various conservation zones

### Infrastructure & Services (~15 POIs)

- **Airport** - Keflavík International, Akureyri, regional airports
- **Lighthouse** - Reykjanesviti, Dyrhólaey, Garðskagi, Grótta
- **Visitor Center** - Major tourist information points
- **Observation Deck** - Perlan, Hallgrímskirkja tower

### Unique Attractions (~25 POIs)

- **Themed Attraction** - Christmas House, exhibitions
- **Viewpoint** - Notable scenic overlooks
- **Cave** - Grjótagjá (non-lava), other caves
- **Bridge** - Notable bridges
- **Photo Spot** - Famous Instagram/photography locations
- **Plane Wreck** - Sólheimasandur DC-3
- **Hiking Trail** - Laugavegur, Fimmvörðuháls, Glymur (major trails only)

---

**Total:** 40+ distinct categories  
**Distribution:** Balanced across all regions of Iceland

**Usage tip:** When unsure, use the simpler category (e.g., "Waterfall" instead of "Glacier-Fed Waterfall"). Consistency is more important than over-specificity.

---

## Data Sources & Search Strategy

### Primary Research Sources

**1. Guide to Iceland** (guidetoiceland.is)
- Most comprehensive English resource
- Detailed descriptions, practical info
- Search: `[POI name] guide to iceland`

**2. Visit Iceland** (visiticeland.com)
- Official tourism authority
- Up-to-date hours, fees
- Search: `[POI name] visit iceland`

**3. Regional Tourism Sites**
- South: south.is
- North: northiceland.is
- West: west.is  
- East: east.is
- Westfjords: westfjords.is

**4. Wikipedia**
- Historical context
- Geological information
- GPS coordinates in infobox
- References for verification

**5. National Parks**
- Vatnajökull: vatnajokulsthjodgardur.is
- Þingvellir: thingvellir.is
- Snæfellsjökull: snaefellsjokull.is

### Search Query Templates

**Overview:**
```
[POI] Iceland description what to see
[POI] Iceland guide information
```

**Coordinates:**
```
[POI] GPS coordinates exact latitude longitude
[POI] Iceland coordinates decimal
```

**Practical Info:**
```
[POI] opening hours admission prices
[POI] visitor information hours
[POI] when to visit best time
```

**Safety:**
```
[POI] Iceland safety warning dangers
[POI] hazards precautions
```

### Search Operators

**For official info:**
```
site:visiticeland.com [POI]
site:*.is [POI]
```

**For coordinates:**
```
"[POI]" GPS coordinates decimal
"[POI]" latitude longitude exact
```

---

## Writing Guidelines

### Description Structure Formula

```
[NAME] is [TYPE] [KEY STAT] [LOCATION]. [More specifics]. 
[Formation/History 1-2 sentences]. [Size/scale with numbers].

[Why special 2-3 sentences]. [Distinctive features]. 
[Geological/cultural significance].

[Visitor experience 2-3 sentences]. [What to see/do]. 
[Additional features]. [Media references if notable].
```

### Word Count by Type

- **Major attractions:** 100-300 words (Jökulsárlón, Dettifoss, Gullfoss)
- **Standard POIs:** 100-200 words (Regional highlights, towns, museums)
- **Simple POIs:** 100-150 words (Swimming pools, restaurants, small sites)

### Style Do's and Don'ts

**✅ DO:**
- Lead with most important facts
- Use specific measurements
- Include concrete details
- Provide historical/geological context
- Mention practical visitor information

**❌ DON'T:**
- Use generic adjectives without explanation
- Include promotional language
- Add personal opinions
- Put pricing in description (goes in opening_hours)
- Repeat POI name too much

---

## GPS Coordinate Verification

### Format Requirements

**Standard format:** `XX.XXXXXX, -XX.XXXXXX`

**Iceland ranges:**
- Latitude: 63.0° to 66.5° N
- Longitude: -13.5° to -24.5° W (NEGATIVE for West)

**Precision:** Minimum 6 decimal places

### Verification Steps

1. **Find from 3 sources:**
   - Wikipedia infobox
   - latitude.to or gps-coordinates.net
   - Official website or Guide to Iceland

2. **Compare coordinates:**
   ```
   Source 1: 64.078400, -16.230600
   Source 2: 64.0784° N, 16.2306° W
   Source 3: 64.0784, -16.2306
   ```

3. **Verify on Google Maps:**
   - Search POI name
   - Right-click → "What's here?"
   - Compare with researched coordinates

4. **Visual check:**
   - Satellite view matches description?
   - On correct road/in correct region?
   - Near correct town?

### Altitude

- Sea level = 0.0
- Highlands = actual elevation in meters
- Can estimate from topographic maps if unknown

---

## Image Sourcing

### Wikimedia Commons Process

1. Go to: commons.wikimedia.org
2. Search: "[POI name] Iceland"
3. Check license (must be public domain or free)
4. Copy URL format: `https://commons.wikimedia.org/wiki/File:[Name].jpg`

### Official Sources

**Acceptable:**
- visiticeland.com
- Regional tourism sites (.is domains)
- Official attraction websites
- National park sites

**NOT acceptable:**
- Instagram, social media
- Personal photography blogs
- Stock photo sites
- Unclear copyright

---

## Quality Checklist

Before marking any POI complete, verify:

### Must-Have Items
- [x] Official English name, correctly spelled
- [x] 100-300 word description with structure
- [x] Complete address with postal code
- [x] GPS coordinates 6+ decimals, verified
- [x] Category from approved taxonomy
- [x] Working website URL or null
- [x] Phone +354 format or null
- [x] 1+ image sources documented
- [x] Opening hours with details
- [x] Rating/reviews or null
- [x] Safety warnings if critical
- [x] Correct JSON filename (lowercase_underscores.json)
- [x] Valid JSON syntax
- [x] Saved to correct directory

### Final Quality Check
- [ ] Description reads naturally?
- [ ] Information useful for tourists?
- [ ] No typos or errors?
- [ ] Current information (2024-2026)?

---

## Examples by POI Type

### Example 1: Major Waterfall (Dettifoss)

**Time:** 18 minutes

**Search queries:**
1. `Dettifoss waterfall Iceland Europe most powerful GPS coordinates`
2. `Dettifoss access routes 862 864`

**Key data found:**
- Europe's most powerful waterfall
- 44m drop, 100m wide, 193-500 m³/s flow
- Vatnajökull National Park
- Two routes: 862 (paved, west) / 864 (gravel, east)
- GPS: 65.814700, -16.384600
- Featured in Prometheus (2012)

**Description approach:**
- Para 1: Power statistics + location
- Para 2: Geological formation + "The Beast" nickname
- Para 3: Access routes + nearby waterfalls

---

### Example 2: Dangerous Beach (Reynisfjara)

**Time:** 20 minutes (extra for safety research)

**Search queries:**
1. `Reynisfjara black sand beach Iceland GPS coordinates`
2. `Reynisfjara safety warning sneaker waves deaths`

**Key data:**
- World's 6th best beach (2021)
- Black volcanic sand, Reynisdrangar stacks
- **CRITICAL: 5 deaths from sneaker waves**
- Hálsanefshellir basalt cave
- GPS: 63.404271, -19.049165

**Special attention:**
- Prominent safety warning in description
- Detailed safety info in opening_hours
- Emphasis on danger throughout

---

### Example 3: Church (Hallgrímskirkja)

**Time:** 15 minutes

**Key data:**
- Tallest church in Iceland (74.5m)
- Built 1945-1986, expressionist style
- 5,275-pipe organ
- Observation deck, panoramic views
- GPS: 64.141716, -21.926638
- Tower admission: 1000 ISK

**Description approach:**
- Para 1: Architecture + physical description
- Para 2: History + basalt column inspiration
- Para 3: Interior + visitor experience

---

### Example 4: Glacier Lagoon (Jökulsárlón)

**Time:** 16 minutes

**Key data:**
- Iceland's deepest lake (284m)
- Formed 1935, quadrupled since 1970s
- 25 km² area
- 1000+ year old icebergs
- Boat tours May-October
- James Bond filming location
- GPS: 64.078400, -16.230600

**Description approach:**
- Para 1: Superlatives + size statistics
- Para 2: Formation + iceberg characteristics
- Para 3: Visitor activities + cultural references

---

## Common Pitfalls

### ❌ Mistakes to Avoid

**1. Too short description**
- Wrong: "Gullfoss is a beautiful waterfall."
- Right: 100-300 words with full structure

**2. Imprecise coordinates**
- Wrong: 64.08, -16.23 (only 2 decimals)
- Right: 64.078400, -16.230600 (6 decimals)

**3. Missing safety warnings**
- Wrong: Reynisfjara as just "beautiful beach"
- Right: Prominent warning about deadly waves

**4. Vague opening hours**
- Wrong: "Open daily"
- Right: "Daily 10:00-17:00 (winter), 09:00-20:00 (summer)"

**5. Wrong file naming**
- Wrong: `Jökulsárlón Glacier Lagoon.json`
- Right: `jokulsarlon_glacier_lagoon.json`

**6. Empty fields**
- Wrong: `"phone": ""`
- Right: `"phone": null`

**7. Promotional language**
- Wrong: "You must visit this amazing place!"
- Right: Factual description of features

**8. Unverified coordinates**
- Wrong: First result only
- Right: Verified from 2-3 sources + Google Maps

**9. Copyright issues**
- Wrong: Instagram photos
- Right: Wikimedia Commons + official sites

**10. Generic categories**
- Wrong: Just "Attraction"
- Right: Specific like "Glacier Lagoon" or "Black Sand Beach"

---

## Time Estimates & Tools

### Time by POI Type

- **Major natural sites:** 15-20 min (waterfalls, glaciers, beaches)
- **Museums/churches:** 12-18 min (need hours research)
- **Towns/cities:** 15-25 min (complex descriptions)
- **Swimming pools:** 10-15 min (simpler, standard format)
- **Restaurants/cafés:** 10-12 min (straightforward)

### Essential Tools

**Coordinates:**
- latitude.to (converter)
- gps-coordinates.net
- Google Maps

**Tourism:**
- guidetoiceland.is
- visiticeland.com
- Regional .is sites

**Images:**
- commons.wikimedia.org
- Official tourism sites

### Workflow Tips

**Batch by region for efficiency:**
1. Do all Golden Circle together
2. Then South Coast
3. Then North Iceland
4. Etc.

**Why:** Overlapping research, fresh geographic context

**Open these tabs:**
1. Google Search
2. Google Maps
3. Wikimedia Commons
4. Text editor for notes
5. Guide to Iceland

---

## JSON Template Reference

```json
{
  "name": "Official Name",
  "description": "100-300 words: What + Why + Experience",
  "address": "Street, Code, Town, Iceland",
  "coordinates": {
    "longitude": -XX.XXXXXX,
    "latitude": XX.XXXXXX,
    "altitude": 0.0
  },
  "rating": 4.7,
  "reviews_count": 15000,
  "category": "Specific Category",
  "website": "https://site.com",
  "phone": "+354 XXX XXXX",
  "images": [
    {
      "source": "Wikimedia Commons",
      "url": "https://commons.wikimedia.org/wiki/File:Name.jpg"
    }
  ],
  "opening_hours": {
    "key": "value"
  }
}
```

---

## Summary

**The Process:**
1-4: Research (search, coordinates, address)
5-6: Write (description, category)
7-11: Details (website, hours, images, ratings, safety)
12-14: Create (JSON file, save, quality check)

**Average Time:** 12-18 minutes per POI  
**Total Project:** 393 POIs × 15 min = ~98 hours  
**Current Status:** See WORK_CHECKLIST.md

**Related Documents:**
- **WORK_CHECKLIST.md** - Pick POIs, track progress
- **PROJECT_SUMMARY.md** - Technical setup, database schema

---

*Last updated: January 9, 2026*  
*Guide version: 2.0 (Consolidated)*  
*POIs completed: 12/393 (3%)*
