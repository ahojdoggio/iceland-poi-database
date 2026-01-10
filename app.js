// Global variables
let allPOIs = [];
let filteredPOIs = [];

// Base path for GitHub Pages (empty for root, or '/repo-name' for project pages)
const BASE_PATH = window.location.pathname.includes('/iceland-poi-database')
    ? '/iceland-poi-database'
    : '';

// Normalize POI data to handle different formats
function normalizePOI(poi) {
    // Handle images - can be strings or objects with url property
    let normalizedImages = [];
    if (poi.images && Array.isArray(poi.images)) {
        normalizedImages = poi.images.map(img => {
            if (typeof img === 'string') {
                return img;
            } else if (img && img.url) {
                return img.url;
            }
            return null;
        }).filter(img => img !== null);
    }
    
    return {
        ...poi,
        images: normalizedImages
    };
}

// Try to load a JSON file, return data or null if not found
async function tryLoadJSON(url) {
    try {
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            // Handle both arrays and single objects
            // If it's a single object, wrap it in an array
            if (Array.isArray(data)) {
                return data;
            } else if (data && typeof data === 'object') {
                return [data];
            }
            return null;
        }
        return null;
    } catch (err) {
        return null;
    }
}

// Load POI files from manifest
async function loadManifestFiles() {
    try {
        const response = await fetch(`${BASE_PATH}/manifest.json`);
        if (!response.ok) {
            console.log('No manifest.json found, skipping manifest-based loading');
            return [];
        }

        const manifest = await response.json();
        const allFiles = [];

        // Load POI files from /pois/ directory
        if (manifest.poi_files && Array.isArray(manifest.poi_files)) {
            const poiPromises = manifest.poi_files.map(filepath => tryLoadJSON(`${BASE_PATH}/${filepath}`));
            const results = await Promise.all(poiPromises);
            results.forEach(data => {
                if (data) allFiles.push(data);
            });
        }

        // Load app folder files
        if (manifest.app_folder_files && Array.isArray(manifest.app_folder_files)) {
            const appPromises = manifest.app_folder_files.map(filename => tryLoadJSON(`${BASE_PATH}/${filename}`));
            const results = await Promise.all(appPromises);
            results.forEach(data => {
                if (data) allFiles.push(data);
            });
        }

        console.log(`Loaded ${allFiles.length} files from manifest`);
        return allFiles;

    } catch (error) {
        console.error('Error loading manifest:', error);
        return [];
    }
}

// Automatically discover and load all database files
async function loadDatabaseFiles() {
    const databaseFiles = [];
    let fileNum = 1;
    let consecutiveFailures = 0;
    const maxFailures = 3; // Stop after 3 consecutive failures
    
    while (consecutiveFailures < maxFailures) {
        const fileNumStr = fileNum.toString().padStart(4, '0');
        const url = `../database/database_${fileNumStr}.json`;
        const data = await tryLoadJSON(url);
        
        if (data) {
            databaseFiles.push(data);
            consecutiveFailures = 0;
        } else {
            consecutiveFailures++;
        }
        
        fileNum++;
    }
    
    return databaseFiles;
}

// Automatically discover and load JSON files from app folder
async function loadAppFolderFiles() {
    const appFiles = [];
    
    // Common JSON filenames that might be in the app folder
    // To add a new JSON file: simply add its filename to this array
    // The app will automatically try to load it
    const commonFiles = [
        'akureyri.json',
        'husavik.json',
        'selfoss.json',
        'reykjavik_main_attractions.json',
        'reykjavik_bars_pubs_clubs.json',
        'reykjavik_swimming_pools.json',
        'waterfalls.json',
        'waterfalls_iceland.json',
        'volcanoes.json',
        'hotsprings.json',
        'golden_circle_attractions.json',
        'southcoast_driving_map.json',
        'iceland_ring_road_attractions.json',
        'westfjords_attractions.json',
        'skaftafell_national_park.json',
        'myvatn_lake_area.json',
        'iceland_towns.json'
    ];
    
    // Try loading common files
    const filePromises = commonFiles.map(filename => tryLoadJSON(filename));
    const results = await Promise.all(filePromises);
    
    results.forEach((data, index) => {
        if (data) {
            appFiles.push(data);
        }
    });
    
    return appFiles;
}

// Load all JSON files automatically without manifest
async function loadAllPOIs() {
    const loadingEl = document.getElementById('loading');
    const gridEl = document.getElementById('poiGrid');
    
    try {
        loadingEl.querySelector('p').textContent = 'Discovering and loading POI files...';

        // Load database files and manifest files in parallel
        const [databaseData, manifestData] = await Promise.all([
            loadDatabaseFiles(),
            loadManifestFiles()
        ]);

        // Flatten all data
        const allFileData = [...databaseData, ...manifestData];
        
        // Flatten and normalize all POIs
        allPOIs = allFileData.flat().map(normalizePOI);
        
        // Remove duplicates based on name (keep first occurrence)
        const seen = new Set();
        allPOIs = allPOIs.filter(poi => {
            const name = poi.name;
            if (seen.has(name)) {
                return false;
            }
            seen.add(name);
            return true;
        });
        
        filteredPOIs = [...allPOIs];
        
        // Update stats
        document.getElementById('totalCount').textContent = allPOIs.length;
        
        // Hide loading, show grid
        loadingEl.style.display = 'none';
        gridEl.style.display = 'grid';
        
        // Render POIs
        renderPOIs(filteredPOIs);

        console.log(`Loaded ${allPOIs.length} unique POIs (${databaseData.flat().length} from database, ${manifestData.flat().length} from manifest)`);
        
    } catch (error) {
        console.error('Error loading POIs:', error);
        loadingEl.innerHTML = '<p style="color: white;">Error loading POIs. Please check the console for details.</p>';
    }
}

// Render POIs to the grid
function renderPOIs(pois) {
    const gridEl = document.getElementById('poiGrid');
    const noResultsEl = document.getElementById('noResults');
    
    if (pois.length === 0) {
        gridEl.style.display = 'none';
        noResultsEl.style.display = 'block';
        return;
    }
    
    gridEl.style.display = 'grid';
    noResultsEl.style.display = 'none';
    
    gridEl.innerHTML = pois.map(poi => createPOICard(poi)).join('');
    
    // Add click handlers to cards
    document.querySelectorAll('.poi-card').forEach((card, index) => {
        card.addEventListener('click', () => {
            openModal(pois[index]);
        });
    });
    
    // Add click handlers to images
    document.querySelectorAll('.poi-image').forEach((img, index) => {
        img.addEventListener('click', (e) => {
            e.stopPropagation();
            openImageModal(img.src);
        });
    });
}

// Create a POI card HTML
function createPOICard(poi) {
    const name = escapeHtml(poi.name || 'Unnamed POI');
    const fullDescription = poi.description || 'No description available.';

    // Check if description is long (more than ~200 characters suggest it will be truncated)
    const needsMore = fullDescription.length > 200;

    // Build description with ...more indicator (before escaping so HTML works)
    let descriptionHtml = escapeHtml(fullDescription);
    if (needsMore) {
        descriptionHtml += ' <span style="color: #667eea; font-weight: 500; cursor: pointer;">...more</span>';
    }

    const category = poi.category || 'uncategorized';
    const hasImages = poi.images && poi.images.length > 0;
    const images = hasImages ? poi.images.slice(0, 3) : [];

    let coordinatesText = '';
    if (poi.coordinates) {
        coordinatesText = `${poi.coordinates.latitude.toFixed(6)}, ${poi.coordinates.longitude.toFixed(6)}`;
    }

    let websiteLink = '';
    if (poi.website) {
        websiteLink = `<div class="poi-detail-item">
            <strong>Website:</strong>
            <a href="${escapeHtml(poi.website)}" target="_blank" class="website-link" onclick="event.stopPropagation()">Visit</a>
        </div>`;
    }

    let addressText = '';
    if (poi.address) {
        addressText = `<div class="poi-detail-item">
            <strong>📍 Address:</strong>
            <span>${escapeHtml(poi.address)}</span>
        </div>`;
    }

    return `
        <div class="poi-card">
            <div class="poi-card-header">
                <div>
                    <div class="poi-name">${name}</div>
                </div>
                <span class="poi-category">${category}</span>
            </div>
            <div class="poi-description">${descriptionHtml}</div>
            ${hasImages ? `
                <div class="poi-images">
                    ${images.map(img => `
                        <img src="${escapeHtml(img)}" alt="${name}" class="poi-image" 
                             onerror="this.style.display='none'">
                    `).join('')}
                </div>
            ` : ''}
            <div class="poi-details">
                ${addressText}
                ${coordinatesText ? `
                    <div class="poi-detail-item">
                        <strong>📍 Coordinates:</strong>
                        <span class="coordinates">${coordinatesText}</span>
                    </div>
                ` : ''}
                ${websiteLink}
            </div>
        </div>
    `;
}

// Open modal with POI details
function openModal(poi) {
    const modal = document.getElementById('poiModal');
    const modalBody = document.getElementById('modalBody');

    const name = escapeHtml(poi.name || 'Unnamed POI');
    const fullDescription = poi.description || 'No description available.';
    const isLongDescription = fullDescription.length > 500;

    // For long descriptions, create truncated version
    let descriptionHtml;
    if (isLongDescription) {
        const truncated = escapeHtml(fullDescription.substring(0, 500));
        const full = escapeHtml(fullDescription);
        descriptionHtml = `
            <div id="modalDescShort">${truncated}...
                <span style="color: #667eea; font-weight: 500; cursor: pointer;" onclick="document.getElementById('modalDescShort').style.display='none'; document.getElementById('modalDescFull').style.display='block';">Read more</span>
            </div>
            <div id="modalDescFull" style="display: none;">
                ${full}
                <span style="color: #667eea; font-weight: 500; cursor: pointer;" onclick="document.getElementById('modalDescFull').style.display='none'; document.getElementById('modalDescShort').style.display='block';"> Read less</span>
            </div>
        `;
    } else {
        descriptionHtml = escapeHtml(fullDescription);
    }

    const category = poi.category || 'uncategorized';
    
    let coordinatesText = '';
    if (poi.coordinates) {
        coordinatesText = `${poi.coordinates.latitude.toFixed(6)}, ${poi.coordinates.longitude.toFixed(6)}`;
    }
    
    let imagesHtml = '';
    if (poi.images && poi.images.length > 0) {
        imagesHtml = `
            <div class="modal-images">
                ${poi.images.map(img => `
                    <img src="${escapeHtml(img)}" alt="${name}" class="modal-image"
                         onclick="openImageModal('${escapeHtml(img)}')"
                         onerror="this.style.display='none'">
                `).join('')}
            </div>
        `;
    }
    
    let websiteLink = '';
    if (poi.website) {
        websiteLink = `
            <div class="poi-detail-item">
                <strong>Website:</strong>
                <a href="${escapeHtml(poi.website)}" target="_blank" class="website-link">${escapeHtml(poi.website)}</a>
            </div>
        `;
    }
    
    let phoneText = '';
    if (poi.phone) {
        phoneText = `
            <div class="poi-detail-item">
                <strong>Phone:</strong>
                <a href="tel:${escapeHtml(poi.phone)}">${escapeHtml(poi.phone)}</a>
            </div>
        `;
    }
    
    let ratingText = '';
    if (poi.rating !== null && poi.rating !== undefined) {
        ratingText = `
            <div class="poi-detail-item">
                <strong>Rating:</strong>
                <span>${poi.rating}${poi.reviews_count ? ` (${poi.reviews_count} reviews)` : ''}</span>
            </div>
        `;
    }
    
    let addressText = '';
    if (poi.address) {
        addressText = `
            <div class="poi-detail-item">
                <strong>Address:</strong>
                <span>${escapeHtml(poi.address)}</span>
            </div>
        `;
    }
    
    let openingHoursText = '';
    if (poi.opening_hours) {
        let hoursHtml = '';
        if (typeof poi.opening_hours === 'object') {
            // Format opening hours with better structure
            const hoursEntries = Object.entries(poi.opening_hours);
            
            // Check if it has structured fields like summer/winter
            if (hoursEntries.length === 1 && hoursEntries[0][0] === 'general') {
                // Simple general hours
                hoursHtml = `<div style="margin-top: 5px;">${escapeHtml(hoursEntries[0][1])}</div>`;
            } else {
                // Multiple fields (summer, winter, etc.) - format as list
                hoursHtml = hoursEntries
                    .map(([key, value]) => {
                        // Capitalize first letter of key
                        const formattedKey = key.charAt(0).toUpperCase() + key.slice(1).replace(/_/g, ' ');
                        return `<div style="margin-top: 8px;"><strong>${escapeHtml(formattedKey)}:</strong><br><span style="margin-left: 10px;">${escapeHtml(value)}</span></div>`;
                    })
                    .join('');
            }
        } else {
            // String format
            hoursHtml = `<div style="margin-top: 5px;">${escapeHtml(poi.opening_hours)}</div>`;
        }
        openingHoursText = `
            <div class="poi-detail-item">
                <strong>Opening Hours:</strong>
                ${hoursHtml}
            </div>
        `;
    }
    
    modalBody.innerHTML = `
        <h2>${name}</h2>
        <div class="poi-description">${descriptionHtml}</div>
        ${imagesHtml}
        <div class="modal-details">
            <div class="poi-detail-item">
                <strong>Category:</strong>
                <span>${category}</span>
            </div>
            ${addressText}
            ${coordinatesText ? `
                <div class="poi-detail-item">
                    <strong>Coordinates:</strong>
                    <span class="coordinates">${coordinatesText}</span>
                </div>
            ` : ''}
            ${websiteLink}
            ${phoneText}
            ${ratingText}
            ${openingHoursText}
        </div>
    `;
    
    modal.style.display = 'block';
}

// Open image in full screen
function openImageModal(imageSrc) {
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.style.display = 'block';
    modal.innerHTML = `
        <div class="modal-content" style="max-width: 90%; padding: 20px;">
            <span class="close" onclick="this.parentElement.parentElement.remove()">&times;</span>
            <img src="${escapeHtml(imageSrc)}" style="width: 100%; border-radius: 8px; cursor: pointer;"
                 onclick="this.parentElement.parentElement.remove()"
                 onerror="this.parentElement.parentElement.remove(); alert('Failed to load image')">
        </div>
    `;
    document.body.appendChild(modal);
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.remove();
        }
    });
}

// Search functionality
function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        
        if (query === '') {
            filteredPOIs = [...allPOIs];
        } else {
            filteredPOIs = allPOIs.filter(poi => {
                const name = (poi.name || '').toLowerCase();
                const description = (poi.description || '').toLowerCase();
                const category = (poi.category || '').toLowerCase();
                const address = (poi.address || '').toLowerCase();
                
                return name.includes(query) || 
                       description.includes(query) || 
                       category.includes(query) ||
                       address.includes(query);
            });
        }
        
        renderPOIs(filteredPOIs);
    });
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('poiModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}

// Close modal with X button
document.querySelector('.close').addEventListener('click', () => {
    document.getElementById('poiModal').style.display = 'none';
});

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    loadAllPOIs();
    setupSearch();
});

