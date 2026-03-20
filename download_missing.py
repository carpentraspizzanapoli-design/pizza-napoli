import urllib.request, urllib.parse, json, time, sys, os
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {'User-Agent': 'PizzaNapoliBot/1.0 (contact@pizzanapolicarpentras.fr)'}
BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli\blog'

def wiki_download(search_term, dest_path, width=900):
    if os.path.exists(dest_path):
        print(f'  SKIP (exists): {dest_path}')
        return True
    # Search
    q = urllib.parse.urlencode({'action':'query','list':'search','srnamespace':'6','srsearch':search_term,'srlimit':'5','format':'json'})
    url = 'https://commons.wikimedia.org/w/api.php?' + q
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        results = data.get('query',{}).get('search',[])
        if not results:
            print(f'  NO RESULT for: {search_term}')
            return False
        title = results[0]['title']
        print(f'  Found: {title}')
        time.sleep(1.5)
        # Get URL
        q2 = urllib.parse.urlencode({'action':'query','titles':title,'prop':'imageinfo','iiprop':'url','iiurlwidth':str(width),'format':'json'})
        req2 = urllib.request.Request('https://commons.wikimedia.org/w/api.php?' + q2, headers=HEADERS)
        with urllib.request.urlopen(req2, timeout=15) as r2:
            d2 = json.loads(r2.read())
        pages = d2['query']['pages']
        page = next(iter(pages.values()))
        img_url = page['imageinfo'][0]['thumburl']
        time.sleep(1.5)
        # Download
        req3 = urllib.request.Request(img_url, headers=HEADERS)
        with urllib.request.urlopen(req3, timeout=30) as r3:
            with open(dest_path, 'wb') as f:
                f.write(r3.read())
        print(f'  OK -> {dest_path}')
        time.sleep(2)
        return True
    except Exception as e:
        print(f'  ERROR: {e}')
        return False

DOWNLOADS = [
    # Monteux
    ('Chapelle Saint-Gens Monteux Vaucluse', r'que-faire-monteux-ce-soir\img\chapelle.jpg'),
    ('Place village Monteux Vaucluse provençal', r'que-faire-monteux-ce-soir\img\place.jpg'),
    # Sarrians
    ('Place centrale village Vaucluse Provence platanes', r'que-faire-sarrians-ce-soir\img\place.jpg'),
    ('Ouveze riviere Provence Vaucluse', r'que-faire-sarrians-ce-soir\img\riviere.jpg'),
    # Caromb
    ('Lac du Paty Caromb Vaucluse', r'que-faire-caromb-ce-soir\img\lac.jpg'),
    ('Caromb village medieval Vaucluse eglise', r'que-faire-caromb-ce-soir\img\village.jpg'),
    # Loriol-du-Comtat
    ('Loriol-du-Comtat village medieval Vaucluse', r'que-faire-loriol-du-comtat-ce-soir\img\village.jpg'),
    ('Cerisiers fleurs Vaucluse Ventoux printemps', r'que-faire-loriol-du-comtat-ce-soir\img\cerisiers.jpg'),
    # Serres
    ('Lac de Serre-Poncon Hautes-Alpes', r'que-faire-serres-ce-soir\img\lac.jpg'),
    ('Vallee du Buech Hautes-Alpes panorama', r'que-faire-serres-ce-soir\img\vallee.jpg'),
]

for term, rel_path in DOWNLOADS:
    dest = os.path.join(BASE, rel_path)
    print(f'\nSearching: {term}')
    wiki_download(term, dest)

print('\nDone.')
