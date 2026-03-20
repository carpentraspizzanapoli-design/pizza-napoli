"""
Générateur de pages locales SEO pour Pizza Napoli Carpentras
Ecrit index.html dans chaque dossier ville existant
"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli'

VILLES = [
    {'slug':'livraison-pizza-carpentras',        'name':'Carpentras',          'cp':'84200','min':2,'delai':'20 à 35 min','lat':44.0506,'lon':5.0497},
    {'slug':'livraison-pizza-pernes-les-fontaines','name':'Pernes-les-Fontaines','cp':'84210','min':3,'delai':'30 à 45 min','lat':43.998,'lon':5.056},
    {'slug':'livraison-pizza-mazan',              'name':'Mazan',               'cp':'84380','min':4,'delai':'35 à 50 min','lat':44.044,'lon':5.119},
    {'slug':'livraison-pizza-monteux',            'name':'Monteux',             'cp':'84170','min':3,'delai':'25 à 40 min','lat':44.026,'lon':5.001},
    {'slug':'livraison-pizza-aubignan',           'name':'Aubignan',            'cp':'84810','min':3,'delai':'20 à 35 min','lat':44.074,'lon':5.026},
    {'slug':'livraison-pizza-loriol-du-comtat',   'name':'Loriol-du-Comtat',    'cp':'84870','min':3,'delai':'25 à 40 min','lat':44.006,'lon':5.011},
    {'slug':'livraison-pizza-caromb',             'name':'Caromb',              'cp':'84330','min':3,'delai':'25 à 40 min','lat':44.107,'lon':5.107},
    {'slug':'livraison-pizza-saint-didier',       'name':'Saint-Didier',        'cp':'84210','min':4,'delai':'35 à 50 min','lat':43.990,'lon':5.100},
    {'slug':'livraison-pizza-serres',             'name':'Serres',              'cp':'84200','min':2,'delai':'20 à 35 min','lat':44.048,'lon':5.042},
]

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Arial,sans-serif;background:#FFFDF7;color:#1A1A1A;overflow-x:hidden}
:root{--r:#CE2B37;--v:#00703C;--o:#C8972A;--c:#FFFDF7;--b:#1A1A1A}
a{color:inherit;text-decoration:none}
.nav{background:rgba(255,255,255,.97);border-bottom:3px solid var(--r);padding:.9rem 2rem;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:99;backdrop-filter:blur(10px);box-shadow:0 2px 10px rgba(0,0,0,.06)}
.nl{font-size:1.05rem;font-weight:700;color:var(--r);letter-spacing:.04em}
.nl span{color:var(--b);font-weight:400}
.nc{background:var(--r);color:#fff;padding:.5rem 1.2rem;font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;font-weight:600;border-radius:2px;transition:background .2s}
.nc:hover{background:#a01f2a}
.hero{background:linear-gradient(135deg,#1a0505,#3d0e0e 50%,#1a1a1a);padding:5rem 2rem 4rem;text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:url('../hero1.jpg') center/cover no-repeat;opacity:.18}
.hc{position:relative;z-index:1}
.hb{display:inline-block;background:rgba(200,151,42,.2);border:1px solid rgba(200,151,42,.5);color:#E8C060;padding:.4rem 1.5rem;font-size:.68rem;letter-spacing:.25em;text-transform:uppercase;margin-bottom:1.2rem;border-radius:2px}
.hero h1{font-size:clamp(1.8rem,5vw,3rem);color:#fff;line-height:1.1;margin-bottom:.8rem}
.hero h1 em{color:#E8C060;font-style:normal}
.hs{font-size:.95rem;color:rgba(255,255,255,.7);margin-bottom:2rem;max-width:480px;margin-left:auto;margin-right:auto;line-height:1.6}
.bg{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.br{background:var(--r);color:#fff;padding:.9rem 2rem;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;font-weight:600;border-radius:2px;transition:all .2s;display:inline-block}
.br:hover{background:#a01f2a;transform:translateY(-2px)}
.bo{border:2px solid rgba(255,255,255,.5);color:#fff;padding:.9rem 2rem;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;font-weight:600;border-radius:2px;transition:all .2s;display:inline-block}
.bo:hover{border-color:#E8C060;color:#E8C060;transform:translateY(-2px)}
.ib{background:var(--r);display:grid;grid-template-columns:repeat(3,1fr);gap:1px}
.ii{background:var(--r);padding:1.4rem;text-align:center;border-right:1px solid rgba(255,255,255,.2)}
.ii:last-child{border-right:none}
.ii .v{font-size:1.6rem;font-weight:700;color:#E8C060;display:block}
.ii .l{font-size:.62rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.7);margin-top:.3rem;display:block}
.pitch{background:var(--b);padding:4rem 2rem}
.pi{max-width:700px;margin:0 auto;text-align:center}
.pi h2{font-size:clamp(1.4rem,3vw,2rem);color:#fff;margin-bottom:1.2rem}
.pi p{color:rgba(255,255,255,.65);line-height:1.8;margin-bottom:1.2rem;font-size:.92rem}
.pbs{display:flex;flex-wrap:wrap;gap:.7rem;justify-content:center;margin-top:1.8rem}
.pb{background:rgba(200,151,42,.15);border:1px solid rgba(200,151,42,.3);color:#E8C060;padding:.45rem 1.1rem;font-size:.76rem;letter-spacing:.08em;border-radius:30px}
.cta{background:var(--c);padding:3.5rem 2rem;text-align:center}
.cta h2{font-size:clamp(1.4rem,3.5vw,2.2rem);margin-bottom:.7rem}
.cta p{color:#666;max-width:480px;margin:0 auto 1.8rem;line-height:1.7;font-size:.9rem}
.zones{background:#f0ede6;padding:3.5rem 2rem}
.zi{max-width:660px;margin:0 auto}
.zi h2{font-size:clamp(1.3rem,3vw,1.9rem);margin-bottom:1.8rem;text-align:center}
table{width:100%;border-collapse:collapse;font-size:.84rem}
th{background:var(--b);color:#E8C060;padding:.65rem 1rem;text-align:left;letter-spacing:.1em;text-transform:uppercase;font-size:.7rem}
tr:nth-child(even){background:#fff}
td{padding:.55rem 1rem;border-bottom:1px solid #e0dbd0}
.cr td{color:var(--r);font-weight:700;background:rgba(206,43,55,.05)}
.faq{background:#fff;padding:3.5rem 2rem}
.fi{max-width:680px;margin:0 auto}
.fi h2{font-size:clamp(1.3rem,3vw,1.9rem);margin-bottom:1.8rem;text-align:center}
details{border:1px solid #e5e0d5;border-radius:3px;margin-bottom:.7rem;overflow:hidden}
summary{padding:.9rem 1.1rem;cursor:pointer;font-weight:600;font-size:.88rem;background:#faf9f5;list-style:none;display:flex;justify-content:space-between;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:'+';font-size:1.1rem;color:var(--r);font-weight:300}
details[open] summary::after{content:'−'}
details div{padding:.9rem 1.1rem;font-size:.88rem;line-height:1.7;color:#555}
.cv{background:var(--b);padding:2.5rem 2rem}
.cvi{max-width:680px;margin:0 auto;text-align:center}
.cvi h3{color:#E8C060;font-size:.7rem;letter-spacing:.25em;text-transform:uppercase;margin-bottom:1rem}
.cp{display:flex;flex-wrap:wrap;gap:.55rem;justify-content:center}
.cpl{background:rgba(200,151,42,.15);border:1px solid rgba(200,151,42,.3);color:rgba(255,255,255,.75);padding:.38rem .95rem;font-size:.76rem;letter-spacing:.05em;border-radius:20px;transition:background .2s}
.cpl:hover{background:rgba(200,151,42,.3);color:#fff}
.cpl.ac{background:var(--r);border-color:var(--r);color:#fff}
footer{background:#111;padding:1.8rem 2rem;text-align:center}
footer p{color:rgba(255,255,255,.35);font-size:.78rem;margin-bottom:.4rem}
footer a{color:#E8C060;text-decoration:underline}
@media(max-width:600px){
  .ib{grid-template-columns:1fr}
  .ii{border-right:none;border-bottom:1px solid rgba(255,255,255,.2)}
  .ii:last-child{border-bottom:none}
}
"""

ZONES = [
    ('Carpentras',2),('Serres',2),('Pernes-les-Fontaines',3),('Monteux',3),
    ('Aubignan',3),('Loriol-du-Comtat',3),('Caromb',3),('Mazan',4),('Saint-Didier',4),
]

def zone_rows(cur_name):
    rows = ''
    for i,(commune,minimum) in enumerate(ZONES):
        is_cur = commune == cur_name
        cls = ' class="cr"' if is_cur else ''
        rows += f'<tr{cls}><td>{"📍 " if is_cur else ""}{commune}</td><td style="text-align:center">{minimum} grande{"s" if minimum>1 else ""} pizza{"s" if minimum>1 else ""}</td></tr>\n'
    return rows

def other_pills(cur_slug):
    pills = ''
    for v in VILLES:
        if v['slug'] == cur_slug: continue
        pills += f'<a href="/{v["slug"]}/" class="cpl">📍 {v["name"]}</a>\n'
    return pills

def gen(v):
    name  = v['name']
    slug  = v['slug']
    cp    = v['cp']
    mp    = v['min']
    delai = v['delai']
    lat   = v['lat']
    lon   = v['lon']
    mt    = f'{mp} grande{"s" if mp>1 else ""} pizza{"s" if mp>1 else ""}'

    h1 = f'Livraison de pizzas à <em>{name}</em>' if name != 'Carpentras' else 'Livraison de pizzas à <em>Carpentras</em> et environs'
    sous = f'Pizza Napoli Carpentras dessert {name} — {mt} minimum' if name != 'Carpentras' else 'Livraison gratuite dès 2 grandes pizzas · 7j/7 · 19h–22h'

    schema = (f'{{"@context":"https://schema.org","@type":"Restaurant",'
              f'"name":"Pizza Napoli Carpentras","url":"https://www.pizzanapolicarpentras.fr/",'
              f'"telephone":"+33761083608","priceRange":"€-€€","servesCuisine":"Pizza",'
              f'"hasMenu":"https://www.pizzanapolicarpentras.fr/#menu",'
              f'"address":{{"@type":"PostalAddress","streetAddress":"209 Avenue Pierre Sémard","addressLocality":"Carpentras","postalCode":"84200","addressCountry":"FR"}},'
              f'"areaServed":[{{"@type":"City","name":"{name}"}},{{"@type":"City","name":"Carpentras"}}],'
              f'"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"17:30","closes":"22:00"}}]}}')

    faq_s = (f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
             f'{{"@type":"Question","name":"Pizza Napoli livre-t-il à {name} ?","acceptedAnswer":{{"@type":"Answer","text":"Oui ! Pizza Napoli Carpentras livre à {name} 7j/7, de 19h à 22h. Minimum {mp} grandes pizzas. Appelez le 07 61 08 36 08."}}}},'
             f'{{"@type":"Question","name":"Quel est le minimum de commande à {name} ?","acceptedAnswer":{{"@type":"Answer","text":"Le minimum est de {mp} grandes pizzas pour une livraison à {name}. Livraison gratuite."}}}},'
             f'{{"@type":"Question","name":"Délai de livraison à {name} ?","acceptedAnswer":{{"@type":"Answer","text":"Le délai est généralement de {delai} pour {name}. Commandez dès 17h30 au 07 61 08 36 08, livraisons dès 19h."}}}}]}}')

    hero_img = '../hero1.jpg' if name != 'Carpentras' else 'hero1.jpg'

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Livraison Pizza {name} — Pizza Napoli Carpentras | 7j/7 dès 19h</title>
<meta name="description" content="Pizza Napoli Carpentras livre vos pizzas à {name} ({cp}) tous les soirs. Minimum {mt}. Livraison gratuite 19h–22h, 7j/7. ☎ 07 61 08 36 08.">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="geo.region" content="FR-84">
<meta name="geo.placename" content="{name}">
<meta name="geo.position" content="{lat};{lon}">
<meta name="ICBM" content="{lat}, {lon}">
<link rel="canonical" href="https://www.pizzanapolicarpentras.fr/{slug}/">
<meta property="og:type" content="website">
<meta property="og:title" content="Livraison Pizza {name} — Pizza Napoli Carpentras">
<meta property="og:description" content="Pizza artisanale livrée à {name}. {mt} minimum. 7j/7 de 19h à 22h. ☎ 07 61 08 36 08">
<meta property="og:url" content="https://www.pizzanapolicarpentras.fr/{slug}/">
<meta property="og:image" content="https://www.pizzanapolicarpentras.fr/hero1.jpg">
<meta property="og:site_name" content="Pizza Napoli Carpentras">
<meta property="og:locale" content="fr_FR">
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{faq_s}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS.replace("url('../hero1.jpg')", "url('" + hero_img + "')")}</style>
</head>
<body>
<nav>
  <a href="/" class="nl">Pizza Napoli <span>Carpentras</span></a>
  <a href="tel:0761083608" class="nc">📞 07 61 08 36 08</a>
</nav>
<div class="hero">
  <div class="hc">
    <div class="hb">Livraison à domicile · Vaucluse · 7j/7</div>
    <h1>{h1}</h1>
    <p class="hs">{sous}</p>
    <div class="bg">
      <a href="tel:0761083608" class="br">📞 Commander maintenant</a>
      <a href="/#menu" class="bo">Voir la carte complète</a>
    </div>
  </div>
</div>
<div class="ib">
  <div class="ii"><span class="v">{mp}</span><span class="l">Pizza{"s" if mp>1 else ""} minimum</span></div>
  <div class="ii"><span class="v" style="font-size:1.2rem">{delai}</span><span class="l">Délai livraison</span></div>
  <div class="ii"><span class="v">19h–22h</span><span class="l">Livraison 7j/7</span></div>
</div>
<div class="pitch">
  <div class="pi">
    <h2>Pizza artisanale livrée chez vous à {name}</h2>
    <p>Pizza Napoli Carpentras est votre pizzeria de référence dans le Vaucluse depuis 2010. Pâte maison fine et croustillante, sauce tomate généreuse, ingrédients frais sélectionnés chaque jour.</p>
    <p>Nous livrons à <strong style="color:#E8C060">{name}</strong> tous les soirs de 19h à 22h. Commandez dès 17h30 par téléphone au <a href="tel:0761083608" style="color:#E8C060;font-weight:700">07 61 08 36 08</a>.</p>
    <div class="pbs">
      <span class="pb">🍕 80+ recettes</span>
      <span class="pb">🫛 Ingrédients frais</span>
      <span class="pb">🔥 Pâte maison</span>
      <span class="pb">🛵 Livraison gratuite</span>
      <span class="pb">⭐ 4,2/5 Google</span>
      <span class="pb">📅 7j/7 dès 17h30</span>
    </div>
  </div>
</div>
<div class="cta">
  <h2>Commander votre pizza à {name}</h2>
  <p>Appelez dès <strong>17h30</strong> · Minimum <strong>{mt}</strong> · Paiement CB, espèces ou tickets restaurant · Livraison gratuite</p>
  <div class="bg">
    <a href="tel:0761083608" class="br">📞 07 61 08 36 08</a>
    <a href="/" class="bo" style="border-color:#aaa;color:#555">Voir le menu</a>
  </div>
</div>
<div class="zones">
  <div class="zi">
    <h2>Zones et minimums de livraison</h2>
    <table>
      <thead><tr><th>Commune</th><th style="text-align:center">Minimum de commande</th></tr></thead>
      <tbody>{zone_rows(name)}</tbody>
    </table>
    <p style="font-size:.76rem;color:#888;margin-top:.8rem;text-align:center">* Livraison gratuite dans toutes les zones</p>
  </div>
</div>
<div class="faq">
  <div class="fi">
    <h2>Questions fréquentes — {name}</h2>
    <details open>
      <summary>Pizza Napoli livre-t-il à {name} ?</summary>
      <div><p>Oui ! <strong>Pizza Napoli Carpentras livre à {name}</strong> 7 jours sur 7, de 19h à 22h. Minimum <strong>{mt}</strong>. Appelez le <a href="tel:0761083608"><strong>07 61 08 36 08</strong></a> dès 17h30.</p></div>
    </details>
    <details>
      <summary>Quel est le minimum de commande pour {name} ?</summary>
      <div><p>Le minimum est de <strong>{mt}</strong> pour une livraison à {name}. La livraison est gratuite. Plus de 80 recettes, dès 7€90 la petite pizza.</p></div>
    </details>
    <details>
      <summary>Quel est le délai de livraison à {name} ?</summary>
      <div><p>Délai estimé : <strong>{delai}</strong>. Commandez dès 17h30 au <a href="tel:0761083608">07 61 08 36 08</a>, les livraisons démarrent à 19h00.</p></div>
    </details>
    <details>
      <summary>Quelles sont les horaires de livraison ?</summary>
      <div><p>Livraison <strong>7 jours sur 7</strong>, de <strong>19h00 à 22h00</strong>. Commandez par téléphone dès 17h30.</p></div>
    </details>
    <details>
      <summary>Quels moyens de paiement sont acceptés ?</summary>
      <div>
        <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0">
          <span style="background:#f5f5f5;border:1px solid #ddd;padding:.38rem .8rem;border-radius:5px;font-size:.85rem;font-weight:600">💳 Carte bancaire</span>
          <span style="background:#f5f5f5;border:1px solid #ddd;padding:.38rem .8rem;border-radius:5px;font-size:.85rem;font-weight:600">💶 Espèces</span>
          <span style="background:#f5f5f5;border:1px solid #ddd;padding:.38rem .8rem;border-radius:5px;font-size:.85rem;font-weight:600">🎫 Tickets restaurant</span>
        </div>
        <p style="color:#c0392b;font-size:.83rem;font-weight:600">✗ Chèques non acceptés</p>
      </div>
    </details>
  </div>
</div>
<div class="cv">
  <div class="cvi">
    <h3>Nous livrons aussi dans ces communes</h3>
    <div class="cp">
      {other_pills(slug)}
    </div>
  </div>
</div>
<footer>
  <p><a href="/">← Retour au site Pizza Napoli Carpentras</a></p>
  <p style="margin-top:.6rem">209 Avenue Pierre Sémard · 84200 Carpentras · <a href="tel:0761083608">07 61 08 36 08</a></p>
  <p style="margin-top:.3rem">Livraison 7j/7 · Carpentras · {name} · Vaucluse</p>
  <p style="margin-top:.6rem;font-size:.7rem;color:rgba(255,255,255,.2)">© 2026 Pizza Napoli Carpentras</p>
</footer>
</body>
</html>"""

# Page Sarrians — non desservi
def gen_sarrians():
    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pizza à Sarrians — Pizza Napoli Carpentras</title>
<meta name="description" content="Pizza Napoli Carpentras ne livre pas encore à Sarrians. Contactez-nous ou venez récupérer votre commande à Carpentras.">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="https://www.pizzanapolicarpentras.fr/">
<script>setTimeout(function(){ window.location.href='/'; }, 4000);</script>
<style>*{box-sizing:border-box;margin:0;padding:0}body{background:#1a0505;font-family:Arial,sans-serif;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;padding:2rem}h1{color:#E8C060;font-size:1.6rem;margin-bottom:1rem}p{color:rgba(255,255,255,.7);line-height:1.7;margin-bottom:1.2rem}a{color:#E8C060}</style>
</head>
<body>
<div>
  <div style="font-size:3rem;margin-bottom:1rem">🛵</div>
  <h1>Sarrians — Zone non desservie</h1>
  <p>Pizza Napoli Carpentras ne livre pas encore à Sarrians.<br>
  Pour toute question, appelez le <a href="tel:0761083608"><strong>07 61 08 36 08</strong></a>.</p>
  <p>Vous pouvez également venir récupérer votre commande directement<br>
  au <strong>209 Avenue Pierre Sémard, Carpentras</strong>.</p>
  <p style="color:rgba(255,255,255,.4);font-size:.85rem">Redirection vers le site principal dans 4 secondes…</p>
  <a href="/" style="display:inline-block;margin-top:1rem;background:#CE2B37;color:#fff;padding:.7rem 1.8rem;border-radius:2px;font-size:.85rem;letter-spacing:.1em">← Retour au site</a>
</div>
</body>
</html>"""

# Générer toutes les pages
for v in VILLES:
    d = os.path.join(BASE, v['slug'])
    os.makedirs(d, exist_ok=True)
    idx = os.path.join(d, 'index.html')
    with open(idx, 'w', encoding='utf-8') as f:
        f.write(gen(v))
    print(f'✓ {v["slug"]}/index.html')

# Sarrians — page non desservie
sarr_dir = os.path.join(BASE, 'livraison-pizza-sarrians')
os.makedirs(sarr_dir, exist_ok=True)
with open(os.path.join(sarr_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(gen_sarrians())
print(f'✓ livraison-pizza-sarrians/index.html (redirect)')

# Sitemap
today = '2026-03-20'
urls = [('https://www.pizzanapolicarpentras.fr/', '1.0', 'daily')]
for v in VILLES:
    urls.append((f'https://www.pizzanapolicarpentras.fr/{v["slug"]}/', '0.8', 'weekly'))

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url, pri, freq in urls:
    sitemap += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>\n'
sitemap += '</urlset>\n'
with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap)
print(f'✓ sitemap.xml ({len(urls)} URLs)')

# robots.txt
with open(os.path.join(BASE, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write('User-agent: *\nAllow: /\nSitemap: https://www.pizzanapolicarpentras.fr/sitemap.xml\n')
print('✓ robots.txt')

print(f'\nDone — {len(VILLES)+1} pages locales générées dans leurs dossiers.')
