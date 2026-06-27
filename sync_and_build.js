const fs = require('fs');
const path = require('path');

const VAULT_ROOT = __dirname;
const QUARTZ_CONTENT_DIR = path.join(VAULT_ROOT, 'quartz-site', 'content');

// Directories/Files to ignore entirely
const IGNORE_LIST = [
    '.git',
    '.obsidian',
    'public-site',
    'quartz-site',
    'sync_and_build.js',
    'node_modules',
    '.gemini'
];

function isIgnored(itemName) {
    return IGNORE_LIST.includes(itemName);
}

function processDirectory(sourceDir, targetDir) {
    const items = fs.readdirSync(sourceDir);

    for (const item of items) {
        if (isIgnored(item)) continue;

        const sourcePath = path.join(sourceDir, item);
        const targetPath = path.join(targetDir, item);

        const stats = fs.statSync(sourcePath);

        if (stats.isDirectory()) {
            if (!fs.existsSync(targetPath)) {
                fs.mkdirSync(targetPath, { recursive: true });
            }
            processDirectory(sourcePath, targetPath);
        } else if (stats.isFile()) {
            // Check if it's a markdown file to apply filtering
            if (item.toLowerCase().endsWith('.md')) {
                const content = fs.readFileSync(sourcePath, 'utf8');
                if (content.includes('#private')) {
                    console.log(`[SKIPPED] Private note: ${sourcePath}`);
                    continue;
                }
            }
            // Copy file
            fs.copyFileSync(sourcePath, targetPath);
        }
    }
}

function run() {
    console.log('--- Starting Vault Sync to Quartz ---');
    
    // Clear quartz content directory first
    if (fs.existsSync(QUARTZ_CONTENT_DIR)) {
        fs.rmSync(QUARTZ_CONTENT_DIR, { recursive: true, force: true });
    }
    fs.mkdirSync(QUARTZ_CONTENT_DIR, { recursive: true });

    // Sync files
    processDirectory(VAULT_ROOT, QUARTZ_CONTENT_DIR);

    // Ensure index.md exists (Quartz requires it for the homepage)
    const indexTarget = path.join(QUARTZ_CONTENT_DIR, 'index.md');
    const readmeTarget = path.join(QUARTZ_CONTENT_DIR, 'README.md');
    
    if (!fs.existsSync(indexTarget)) {
        if (fs.existsSync(readmeTarget)) {
            fs.copyFileSync(readmeTarget, indexTarget);
            console.log('[INFO] Copied README.md to index.md');
        } else {
            fs.writeFileSync(indexTarget, '# Welcome to my Digital Garden\n\nThis is the home page of my public notes.');
            console.log('[INFO] Created a default index.md');
        }
    }

    console.log('--- Sync Complete! ---');
}

run();
