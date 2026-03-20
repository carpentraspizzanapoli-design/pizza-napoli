import shutil, os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli\blog'

def src(folder, name):
    return os.path.join(BASE, folder, 'img', name)

def dst(folder, name):
    return os.path.join(BASE, folder, 'img', name)

def copy(s, d):
    if os.path.exists(s):
        shutil.copy2(s, d)
        print(f'COPY {os.path.basename(s)} -> {d.split(chr(92))[-3]}/{os.path.basename(d)}')
    else:
        print(f'SOURCE MISSING: {s}')

def delete(d):
    if os.path.exists(d):
        os.remove(d)
        print(f'DELETE {d.split(chr(92))[-3]}/{os.path.basename(d)}')

# --- MONTEUX: chapelle.jpg est un PDF, place.jpg manque ---
delete(dst('que-faire-monteux-ce-soir', 'chapelle.jpg'))  # bad PDF
# chapelle (panorama) -> mont_ventoux from carpentras
copy(src('que-faire-carpentras-ce-soir', 'mont_ventoux.jpg'), dst('que-faire-monteux-ce-soir', 'chapelle.jpg'))
# place du village -> place_carpentras from carpentras
copy(src('que-faire-carpentras-ce-soir', 'place_carpentras.jpg'), dst('que-faire-monteux-ce-soir', 'place.jpg'))

# --- SARRIANS: place.jpg = BMX (mauvais), riviere.jpg = mauvaise rivière ---
delete(dst('que-faire-sarrians-ce-soir', 'place.jpg'))
delete(dst('que-faire-sarrians-ce-soir', 'riviere.jpg'))
# place du village -> use vignoble from mazan (paysage provençal)
copy(src('que-faire-mazan-ce-soir', 'vignoble.jpg'), dst('que-faire-sarrians-ce-soir', 'place.jpg'))
# rivière -> use dentelles.jpg from aubignan (paysage vaucluse)
copy(src('que-faire-aubignan-ce-soir', 'dentelles.jpg'), dst('que-faire-sarrians-ce-soir', 'riviere.jpg'))

# --- CAROMB: village.jpg manque (lac.jpg est bon) ---
# village médiéval -> use porte_nd from pernes (porte médiévale = OK visuellement)
copy(src('que-faire-pernes-les-fontaines-ce-soir', 'porte_nd.jpg'), dst('que-faire-caromb-ce-soir', 'village.jpg'))

# --- LORIOL: village.jpg potentiellement OK, cerisiers manque ---
# cerisiers -> use vignes.jpg from aubignan (campagne vaucluse)
copy(src('que-faire-aubignan-ce-soir', 'vignes.jpg'), dst('que-faire-loriol-du-comtat-ce-soir', 'cerisiers.jpg'))

print('\nDone.')
