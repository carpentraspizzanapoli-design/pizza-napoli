import urllib.request, urllib.parse, json, time, sys, os
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {'User-Agent': 'PizzaNapoliBot/1.0 (contact@pizzanapolicarpentras.fr)'}
BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli\blog'

def download_file(title, dest_path, width=900):
    if os.path.exists(dest_path):
        os.remove(dest_path)  # re-download to fix bad ones
    q = urllib.parse.urlencode({'action':'query','titles':title,'prop':'imageinfo','iiprop':'url','iiurlwidth':str(width),'format':'json'})
    req = urllib.request.Request('https://commons.wikimedia.org/w/api.php?' + q, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        pages = d['query']['pages']
        page = next(iter(pages.values()))
        img_url = page['imageinfo'][0]['thumburl']
        time.sleep(1.5)
        req2 = urllib.request.Request(img_url, headers=HEADERS)
        with urllib.request.urlopen(req2, timeout=30) as r2:
            content = r2.read()
        with open(dest_path, 'wb') as f:
            f.write(content)
        print(f'OK ({len(content)} bytes) -> {os.path.basename(dest_path)}')
        time.sleep(2)
        return True
    except Exception as e:
        print(f'ERROR: {e}')
        return False

DOWNLOADS = [
    # Fix bad ones + add missing
    ('File:Chapelle Saint-Gens (Monteux, Vaucluse, France).jpg',
     r'que-faire-monteux-ce-soir\img\chapelle.jpg'),
    ('File:Monteux (Vaucluse).jpg',
     r'que-faire-monteux-ce-soir\img\place.jpg'),
    # Sarrians - fix bad place.jpg
    ('File:Sarrians (Vaucluse) - place de la mairie.jpg',
     r'que-faire-sarrians-ce-soir\img\place.jpg'),
    ('File:Ouveze a Vaison la Romaine.jpg',
     r'que-faire-sarrians-ce-soir\img\riviere.jpg'),
    # Caromb village (lac already OK)
    ('File:Caromb (Vaucluse) - eglise Saint-Maurice.jpg',
     r'que-faire-caromb-ce-soir\img\village.jpg'),
    # Loriol
    ('File:Aqueduc des Cinq-Cantons (Loriol-du-Comtat).jpg',
     r'que-faire-loriol-du-comtat-ce-soir\img\village.jpg'),
    ('File:Cerisiers en fleurs - Vaucluse (2).jpg',
     r'que-faire-loriol-du-comtat-ce-soir\img\cerisiers.jpg'),
    # Serres
    ('File:Serres (Hautes-Alpes) - vue générale.jpg',
     r'que-faire-serres-ce-soir\img\vallee.jpg'),
]

for title, rel_path in DOWNLOADS:
    dest = os.path.join(BASE, rel_path)
    print(f'Downloading: {title}')
    download_file(title, dest)

print('\nDone.')
