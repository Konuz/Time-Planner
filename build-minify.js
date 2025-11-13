const fs = require('fs');
const path = require('path');
const { minify } = require('html-minifier-terser');

(async () => {
    console.log('🔨 Time Planner - Minification Build Process');
    console.log('=============================================');

    const sourceFile = path.join(__dirname, 'src', 'index.html');
    const distDir = path.join(__dirname, 'src-dist');
    const distFile = path.join(distDir, 'index.html');

    // Sprawdź czy plik źródłowy istnieje
    if (!fs.existsSync(sourceFile)) {
        console.error(`❌ Source file not found: ${sourceFile}`);
        process.exit(1);
    }

    console.log(`📖 Reading: ${sourceFile}`);
    const html = fs.readFileSync(sourceFile, 'utf8');
    console.log(`   Size: ${html.length.toLocaleString()} bytes`);

    console.log('🗜️  Minifying HTML/CSS/JS...');
    const minified = await minify(html, {
        collapseWhitespace: true,
        removeComments: true,
        minifyCSS: true,
        minifyJS: true,
        removeAttributeQuotes: true,
        conservativeCollapse: true,
        preserveLineBreaks: false,
        removeRedundantAttributes: true,
        removeScriptTypeAttributes: true,
        removeStyleLinkTypeAttributes: true,
        useShortDoctype: true
    });

    // Utwórz folder dist jeśli nie istnieje
    if (!fs.existsSync(distDir)) {
        console.log(`📁 Creating directory: ${distDir}`);
        fs.mkdirSync(distDir, { recursive: true });
    }

    console.log(`💾 Writing: ${distFile}`);
    fs.writeFileSync(distFile, minified, 'utf8');

    // Kopiuj czcionki
    const fontsSource = path.join(__dirname, 'src', 'fonts');
    const fontsDest = path.join(distDir, 'fonts');

    if (fs.existsSync(fontsSource)) {
        console.log('📦 Copying fonts...');
        if (!fs.existsSync(fontsDest)) {
            fs.mkdirSync(fontsDest, { recursive: true });
        }
        fs.cpSync(fontsSource, fontsDest, { recursive: true });
        console.log('   ✅ Fonts copied');
    }

    // Kopiuj tłumaczenia
    const translationsSource = path.join(__dirname, 'src', 'translations');
    const translationsDest = path.join(distDir, 'translations');

    if (fs.existsSync(translationsSource)) {
        console.log('📋 Copying translations...');
        if (!fs.existsSync(translationsDest)) {
            fs.mkdirSync(translationsDest, { recursive: true });
        }

        const translationFiles = fs.readdirSync(translationsSource).filter(f => f.endsWith('.json'));
        translationFiles.forEach(file => {
            fs.copyFileSync(
                path.join(translationsSource, file),
                path.join(translationsDest, file)
            );
        });
        console.log(`   ✅ ${translationFiles.length} translation files copied`);
    }

    // Podsumowanie
    const reduction = Math.round((1 - minified.length / html.length) * 100);
    const saved = html.length - minified.length;

    console.log('\n✅ Build completed successfully!');
    console.log('=============================================');
    console.log(`   Original:  ${html.length.toLocaleString()} bytes`);
    console.log(`   Minified:  ${minified.length.toLocaleString()} bytes`);
    console.log(`   Saved:     ${saved.toLocaleString()} bytes (${reduction}%)`);
    console.log(`   Output:    ${distDir}`);
    console.log('=============================================\n');
})().catch(error => {
    console.error('❌ Build failed:', error);
    process.exit(1);
});
