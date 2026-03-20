import urllib.request, urllib.parse, json, time, sys, os
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {'User-Agent': 'PizzaNapoliBot/1.0 (contact@pizzanapolicarpentras.fr)'}
BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli\blog'

def search_and_download(search_term, dest_path, width=900):
    q = urllib.parse.urlencode({'action':'query','list':'search','srnamespace':'6',
        'srsearch':search_term,'srlimit':'10','format':'json'})
    req = urllib.request.Request('https://commons.wikimedia.org/w/api.php?' + q, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        results = data.get('query',{}).get('search',[])
        # Filter: only jpg/png, no pdf
        results = [r for r in results if any(r['title'].lower().endswith(ext) for ext in ('.jpg','.jpeg','.png','.JPG'))]
        if not results:
            print(f'  NO IMAGE RESULT for: {search_term}')
            return False
        title = results[0]['title']
        print(f'  Found: {title}')
        time.sleep(1.5)
        q2 = urllib.parse.urlencode({'action':'query','titles':title,'prop':'imageinfo',
            'iiprop':'url','iiurlwidth':str(width),'format':'json'})
        req2 = urllib.request.Request('https://commons.wikimedia.org/w/api.php?' + q2, headers=HEADERS)
        with urllib.request.urlopen(req2, timeout=15) as r2:
            d2 = json.loads(r2.read())
        pages = d2['query']['pages']
        page = next(iter(pages.values()))
        img_url = page['imageinfo'][0]['thumburl']
        time.sleep(1.5)
        req3 = urllib.request.Request(img_url, headers=HEADERS)
        with urllib.request.urlopen(req3, timeout=30) as r3:
            content = r3.read()
        if os.path.exists(dest_path):
            os.remove(dest_path)
        with open(dest_path, 'wb') as f:
            f.write(content)
        print(f'  OK ({len(content)} bytes) -> {os.path.basename(dest_path)}')
        time.sleep(2)
        return True
    except Exception as e:
        print(f'  ERROR: {e}')
        return False

DOWNLOADS = [
    # Monteux
    ('Monteux Vaucluse chapelle village', r'que-faire-monteux-ce-soir\img\chapelle.jpg'),
    ('Monteux village Vaucluse', r'que-faire-monteux-ce-soir\img\place.jpg'),
    # Sarrians
    ('Sarrians Vaucluse village', r'que-faire-sarrians-ce-soir\img\place.jpg'),
    ('Ouveze riviere Vaucluse', r'que-faire-sarrians-ce-soir\img\riviere.jpg'),
    # Caromb
    ('Caromb village eglise Vaucluse', r'que-faire-caromb-ce-soir\img\village.jpg'),
    # Loriol
    ('Loriol Comtat village Vaucluse', r'que-faire-loriol-du-comtat-ce-soir\img\village.jpg'),
    ('cerisiers fleurs Vaucluse printemps', r'que-faire-loriol-du-comtat-ce-soir\img\cerisiers.jpg'),
    # Serres
    ('Serres Hautes-Alpes village', r'que-faire-serres-ce-soir\img\vallee.jpg'),
]

for term, rel_path in DOWNLOADS:
    dest = os.path.join(BASE, rel_path)
    print(f'\nSearching: {term}')
    search_and_download(term, dest)

print('\nDone.')
