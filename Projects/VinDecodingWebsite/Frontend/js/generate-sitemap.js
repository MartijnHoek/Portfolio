const fs = require('fs');
const path = require('path');

const baseUrl = 'https://vintrospect.com';
const outputFile = path.join(__dirname, 'sitemap.xml');

const foldersToScan = [
    path.join(__dirname, '..'),           // /core
    path.join(__dirname, '..', 'pages')   // /core/pages
];

const urls = [];

function walkDir(dir) {
    if (!fs.existsSync(dir)) return;
    fs.readdirSync(dir).forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            walkDir(fullPath);
        } else if (file.endsWith('.html')) {
            const relativePath = path.relative(path.join(__dirname, '..'), fullPath).replace(/\\/g, '/');
            let loc = relativePath.replace(/index\.html$/, '');
            loc = loc.replace(/\.html$/, '');
            loc = '/' + loc;
            urls.push(loc);
        }
    });
}

foldersToScan.forEach(folder => walkDir(folder));

let sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n`;
sitemap += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;
urls.forEach(url => {
    sitemap += `  <url>\n`;
    sitemap += `    <loc>${baseUrl}${url}</loc>\n`;
    sitemap += `    <lastmod>${new Date().toISOString()}</lastmod>\n`;
    sitemap += `  </url>\n`;
});
sitemap += `</urlset>`;

fs.writeFileSync(outputFile, sitemap);
console.log(`Sitemap generated with ${urls.length} URLs at ${outputFile}`);
