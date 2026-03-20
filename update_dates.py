import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE_BLOG = r'C:\Users\xxx\Desktop\code claude\pizza-napoli\blog'
BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli'

# Dates étalées sur 2-3 mois
DATES = {
    'guide-livraison-pizza-carpentras':    ('2026-01-08', '8 janvier 2026'),
    'pizza-artisanale-carpentras':         ('2026-01-15', '15 janvier 2026'),
    'meilleures-pizzas-carpentras':        ('2026-01-28', '28 janvier 2026'),
    'pate-pizza-maison-carpentras':        ('2026-02-05', '5 février 2026'),
    'commander-pizza-groupe-carpentras':   ('2026-02-19', '19 février 2026'),
    'faq-livraison-pizza-carpentras':      ('2026-03-03', '3 mars 2026'),
    'que-faire-carpentras-ce-soir':        ('2026-03-10', '10 mars 2026'),
    'que-faire-mazan-ce-soir':             ('2026-03-11', '11 mars 2026'),
    'que-faire-monteux-ce-soir':           ('2026-03-12', '12 mars 2026'),
    'que-faire-pernes-les-fontaines-ce-soir': ('2026-03-13', '13 mars 2026'),
    'que-faire-aubignan-ce-soir':          ('2026-03-14', '14 mars 2026'),
    'que-faire-sarrians-ce-soir':          ('2026-03-15', '15 mars 2026'),
    'que-faire-caromb-ce-soir':            ('2026-03-16', '16 mars 2026'),
    'que-faire-loriol-du-comtat-ce-soir':  ('2026-03-17', '17 mars 2026'),
    'que-faire-saint-didier-ce-soir':      ('2026-03-17', '17 mars 2026'),
    'que-faire-serres-ce-soir':            ('2026-03-18', '18 mars 2026'),
}

for slug, (iso, fr) in DATES.items():
    path = os.path.join(BASE_BLOG, slug, 'index.html')
    if not os.path.exists(path):
        print(f'NOT FOUND: {slug}')
        continue
    with open(path, encoding='utf-8') as f:
        html = f.read()

    # JSON-LD: datePublished and dateModified
    html = re.sub(r'"datePublished":"[^"]*"', f'"datePublished":"{iso}"', html)
    html = re.sub(r'"dateModified":"[^"]*"', f'"dateModified":"{iso}"', html)
    # Visible date text (article-meta)
    html = re.sub(r'Publié le \d+ \w+ 2026', f'Publié le {fr}', html)
    # Also handle "Publié le 18 mars 2026" with different formats
    html = re.sub(r'18 mars 2026', fr, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK {slug} -> {iso}')

# Sitemap
SITEMAP_DATES = {
    '/blog/guide-livraison-pizza-carpentras/':    '2026-01-08',
    '/blog/pizza-artisanale-carpentras/':         '2026-01-15',
    '/blog/meilleures-pizzas-carpentras/':        '2026-01-28',
    '/blog/pate-pizza-maison-carpentras/':        '2026-02-05',
    '/blog/commander-pizza-groupe-carpentras/':   '2026-02-19',
    '/blog/faq-livraison-pizza-carpentras/':      '2026-03-03',
    '/blog/que-faire-carpentras-ce-soir/':        '2026-03-10',
    '/blog/que-faire-mazan-ce-soir/':             '2026-03-11',
    '/blog/que-faire-monteux-ce-soir/':           '2026-03-12',
    '/blog/que-faire-pernes-les-fontaines-ce-soir/': '2026-03-13',
    '/blog/que-faire-aubignan-ce-soir/':          '2026-03-14',
    '/blog/que-faire-sarrians-ce-soir/':          '2026-03-15',
    '/blog/que-faire-caromb-ce-soir/':            '2026-03-16',
    '/blog/que-faire-loriol-du-comtat-ce-soir/':  '2026-03-17',
    '/blog/que-faire-saint-didier-ce-soir/':      '2026-03-17',
    '/blog/que-faire-serres-ce-soir/':            '2026-03-18',
}

sitemap_path = os.path.join(BASE, 'sitemap.xml')
with open(sitemap_path, encoding='utf-8') as f:
    sitemap = f.read()

for url_path, iso in SITEMAP_DATES.items():
    # Match the block containing this URL and replace its lastmod
    pattern = r'(<loc>https://www\.pizzanapolicarpentras\.fr' + re.escape(url_path) + r'</loc>\s*<lastmod>)[^<]*(</lastmod>)'
    sitemap = re.sub(pattern, rf'\g<1>{iso}\2', sitemap)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)
print(f'\nSitemap updated.')
print('Done.')
