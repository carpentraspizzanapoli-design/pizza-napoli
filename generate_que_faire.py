import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\xxx\Desktop\code claude\pizza-napoli\blog'
SITE = 'https://www.pizzanapolicarpentras.fr'

CSS_SRC = open(os.path.join(BASE, 'que-faire-carpentras-ce-soir', 'index.html'), encoding='utf-8').read()
m = re.search(r'<style>(.*?)</style>', CSS_SRC, re.DOTALL)
STYLE = m.group(1) if m else ''
if 'ville-photo' not in STYLE:
    STYLE += """
    .ville-photo{border-radius:8px;overflow:hidden;margin:1rem 0;box-shadow:0 2px 8px rgba(0,0,0,.1);}
    .ville-photo img{width:100%;height:220px;object-fit:cover;display:block;}
    .ville-photo a{display:block;position:relative;}
    .ville-photo-caption{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,.7));color:#fff;padding:.5rem .8rem;font-size:.8rem;font-weight:600;}
    .sortie-photo{border-radius:6px;overflow:hidden;margin:.8rem 0;box-shadow:0 2px 6px rgba(0,0,0,.08);}
    .sortie-photo a{display:block;position:relative;}
    .sortie-photo img{width:100%;height:180px;object-fit:cover;display:block;transition:transform .3s;}
    .sortie-photo:hover img{transform:scale(1.02);}
    .sortie-photo-cap{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,.65));color:#fff;padding:.4rem .7rem;font-size:.75rem;font-weight:600;}"""

DATES = {
    'mazan':                  '2026-03-11',
    'monteux':                '2026-03-12',
    'pernes-les-fontaines':   '2026-03-13',
    'aubignan':               '2026-03-14',
    'sarrians':               '2026-03-15',
    'caromb':                 '2026-03-16',
    'loriol-du-comtat':       '2026-03-17',
    'saint-didier':           '2026-03-17',
    'serres':                 '2026-03-18',
}

TOWNS = [
  {'slug':'mazan','nom':'Mazan','cp':'84380','dept':'Vaucluse',
   'desc':'village du Comtat Venaissin, berceau du Marquis de Sade',
   'meta':'Sarcophages romains, château du Marquis de Sade, vignobles du Ventoux... Que faire à Mazan ce soir ? Idées de sorties + pizza livrée.',
   'intro':"Mazan est l'un des villages les mieux préservés du Comtat Venaissin. Il dissimule un patrimoine surprenant : une nécropole romaine unique, un château chargé d'histoire, et les premiers contreforts du Mont Ventoux en toile de fond.",
   'sorties':[
     {'t':"La nécropole et les sarcophages romains",'img':'arc.jpg','alt':'Patrimoine romain Vaucluse','maps':'Sarcophages+romains+Mazan+Vaucluse','cap':'📍 Nécropole romaine de Mazan',
      'txt':"Le long de la route de Mazan, une soixantaine de <a href='https://www.google.com/maps/dir/?api=1&destination=Sarcophages+romains+Mazan+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>sarcophages romains du IIIe siècle</strong></a> sont alignés sur plusieurs dizaines de mètres. Une nécropole à l'air libre, gratuite et toujours accessible — un spectacle archéologique rare en France.",
      'pizza':"La Romaine — tomate, anchois, olives. En hommage à l'époque romaine."},
     {'t':"Le château du Marquis de Sade",'img':'chateau.jpg','alt':'Château de Mazan Vaucluse','maps':'Château+de+Mazan+Vaucluse','cap':'📍 Château de Mazan',
      'txt':"Le <a href='https://www.google.com/maps/dir/?api=1&destination=Château+de+Mazan+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>château de Mazan</strong></a>, ancienne propriété du Marquis de Sade, est aujourd'hui un hôtel élégant. Sa façade classique cache une histoire sulfureuse que l'on peut imaginer en flânant autour du parc.",
      'pizza':"La Tartufo — truffe noire, mozza di bufala. Un luxe à la hauteur du château."},
     {'t':"Balade dans les vignobles du Ventoux",'img':'vignoble.jpg','alt':'Vignoble AOC Ventoux Vaucluse','maps':'Vignobles+Ventoux+Mazan+Vaucluse','cap':'📍 Vignobles AOC Ventoux',
      'txt':"Mazan est au cœur de l'<a href='https://www.google.com/maps/dir/?api=1&destination=Vignobles+Ventoux+Mazan+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>AOC Ventoux</strong></a>. En soirée, une balade dans les vignes offre une vue dégagée sur le sommet. Les caves locales ouvrent leurs portes à la dégustation.",
      'pizza':"La Margharita — simple, directe, comme une soirée dans les vignes."},
   ]},
  {'slug':'monteux','nom':'Monteux','cp':'84170','dept':'Vaucluse',
   'desc':'village provençal entre Carpentras et le Rhône, terre de lavande et de Saint-Gens',
   'meta':'Chapelle Saint-Gens, champs de lavande, tour médiévale... Que faire à Monteux ce soir ? Idées de sorties + pizza livrée.',
   'intro':"Monteux est un village discret du Comtat Venaissin posé entre Carpentras et le Rhône. On y vient pour la chapelle Saint-Gens, les champs de lavande, et l'atmosphère tranquille d'un village provençal.",
   'sorties':[
     {'t':"La chapelle Saint-Gens et son panorama",'img':'chapelle.jpg','alt':'Panorama Comtat Venaissin Mont Ventoux','maps':'Chapelle+Saint-Gens+Monteux+Vaucluse','cap':'📍 Chapelle Saint-Gens — vue sur le Comtat',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Chapelle+Saint-Gens+Monteux+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>chapelle Saint-Gens</strong></a> est un lieu de pèlerinage actif depuis le Moyen Âge. La montée à pied offre un panorama exceptionnel sur la plaine du Comtat avec le Ventoux en arrière-plan.",
      'pizza':"La Chèvre-Miel — douce et parfumée, comme la montée vers la chapelle."},
     {'t':"Les champs de lavande du plateau",'img':'lavande.jpg','alt':'Lavande en fleur Provence été','maps':'Lavande+Monteux+Vaucluse','cap':'📍 Lavande de Provence',
      'txt':"En juin-juillet, les <a href='https://www.google.com/maps/dir/?api=1&destination=Lavande+Monteux+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>champs de lavande</strong></a> autour de Monteux offrent un spectacle violet et parfumé. Quelques kilomètres à pied ou à vélo suffisent pour se retrouver au milieu des rangées bleues.",
      'pizza':"La Provençale — herbes de Provence, tomates confites. Le prolongement naturel."},
     {'t':"La place du village et ses platanes",'img':'place.jpg','alt':'Place provençale village Vaucluse platanes','maps':'Centre+Monteux+Vaucluse','cap':'📍 Centre de Monteux',
      'txt':"La place centrale de <a href='https://www.google.com/maps/dir/?api=1&destination=Centre+Monteux+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>Monteux</strong></a> et ses platanes centenaires sont faits pour s'attarder. Un café, des habitants qui jouent aux boules — la Provence dans toute son authenticité.",
      'pizza':"La Reine — intemporelle, comme ces ruelles de pierre."},
   ]},
  {'slug':'pernes-les-fontaines','nom':'Pernes-les-Fontaines','cp':'84210','dept':'Vaucluse',
   'desc':'la ville aux 40 fontaines, joyau médiéval du Vaucluse',
   'meta':"Pernes-les-Fontaines et ses 40 fontaines, Tour Ferrande, remparts médiévaux... Que faire à Pernes ce soir ? 4 idées + pizza livrée.",
   'intro':"Pernes-les-Fontaines est l'une des villes les plus attachantes du Vaucluse. Ancienne capitale du Comtat Venaissin, elle compte plus de 40 fontaines réparties dans ses ruelles médiévales. Le soir éclairées, elles créent une atmosphère unique.",
   'sorties':[
     {'t':"Le circuit des 40 fontaines",'img':'fontaine.jpg','alt':'Fontaine Reboul Pernes-les-Fontaines','maps':'Fontaines+Pernes-les-Fontaines+Vaucluse','cap':'📍 Fontaine Reboul — Pernes',
      'txt':"Plus de <a href='https://www.google.com/maps/dir/?api=1&destination=Fontaines+Pernes-les-Fontaines+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>40 fontaines</strong></a> jaillissent dans les ruelles de Pernes. Le circuit piéton prend 45 minutes et se découvre facilement en soirée — l'éclairage crée une atmosphère très particulière.",
      'pizza':"La 4 Fromages — généreuse, comme la ville l'est avec ses fontaines."},
     {'t':"La Tour Ferrande et ses fresques médiévales",'img':'tour_ferrande.jpg','alt':'Tour Ferrande Pernes-les-Fontaines','maps':'Tour+Ferrande+Pernes-les-Fontaines','cap':'📍 Tour Ferrande',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Tour+Ferrande+Pernes-les-Fontaines' target='_blank' rel='noopener noreferrer'><strong>Tour Ferrande</strong></a> abrite l'un des plus anciens cycles de fresques profanes de France (XIIIe siècle). Une visite guidée sur réservation — une découverte rare.",
      'pizza':"La Milano — fine et élaborée, à l'image de ces fresques d'exception."},
     {'t':"La Porte Notre-Dame et son pont médiéval",'img':'porte_nd.jpg','alt':'Porte Notre-Dame Pernes-les-Fontaines','maps':'Porte+Notre-Dame+Pernes-les-Fontaines','cap':'📍 Porte Notre-Dame',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Porte+Notre-Dame+Pernes-les-Fontaines' target='_blank' rel='noopener noreferrer'><strong>Porte Notre-Dame</strong></a> avec sa chapelle au-dessus du pont médiéval est l'une des images les plus photographiées du Vaucluse. En fin de journée, le reflet dans la Nesque est un tableau provençal parfait.",
      'pizza':"La Margharita — classique comme ce pont qui traverse les siècles."},
   ]},
  {'slug':'aubignan','nom':'Aubignan','cp':'84810','dept':'Vaucluse',
   'desc':'village vigneron au pied des Dentelles de Montmirail',
   'meta':"Cave viticole AOC Ventoux, Dentelles de Montmirail, vignes et oliviers... Que faire à Aubignan ce soir ? Idées + pizza livrée.",
   'intro':"Aubignan est un village vigneron authentique du Vaucluse, posé entre Carpentras et les Dentelles de Montmirail. Pas de tourisme de masse ici : des vignes, des caves coopératives, et une vue sur les Dentelles qui coupe le souffle.",
   'sorties':[
     {'t':"La cave coopérative et les vins du Ventoux",'img':'cave.jpg','alt':'Cave vinicole Vaucluse extérieur','maps':'Cave+coopérative+Aubignan+Vaucluse','cap':'📍 Cave coopérative d\'Aubignan',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Cave+coopérative+Aubignan+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>cave coopérative d'Aubignan</strong></a> produit des vins AOC Ventoux reconnus. Dégustation en fin de journée directement à la propriété — une façon simple de découvrir ce terroir.",
      'pizza':"La Tartufo — accord parfait avec un verre de Ventoux rouge."},
     {'t':"Vue panoramique sur les Dentelles de Montmirail",'img':'dentelles.jpg','alt':'Dentelles de Montmirail village Vaucluse','maps':'Dentelles+de+Montmirail+Vaucluse','cap':'📍 Dentelles de Montmirail',
      'txt':"Depuis les hauteurs d'Aubignan, les <a href='https://www.google.com/maps/dir/?api=1&destination=Dentelles+de+Montmirail+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>Dentelles de Montmirail</strong></a> se découpent sur le ciel avec une précision saisissante. En soirée, les derniers rayons les teintent de rouge et d'or.",
      'pizza':"La Cochonnaille — généreuse comme ces paysages."},
     {'t':"Balade dans les vignes et les oliviers",'img':'vignes.jpg','alt':'Vignes oliviers Vaucluse Provence','maps':'Vignes+Aubignan+Vaucluse','cap':'📍 Vignes et oliviers du Vaucluse',
      'txt':"Les chemins entre <a href='https://www.google.com/maps/dir/?api=1&destination=Vignes+Aubignan+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>vignes et oliviers</strong></a> autour d'Aubignan sont praticables à pied ou à vélo. En été, l'odeur de la garrigue mêlée aux vignes est une expérience olfactive à part entière.",
      'pizza':"La Margharita à l'huile d'olive — ici, c'est obligatoire."},
   ]},
  {'slug':'sarrians','nom':'Sarrians','cp':'84260','dept':'Vaucluse',
   'desc':'village de la plaine du Comtat, entre Rhône et vignobles',
   'meta':"Village provençal, vignobles Côtes-du-Rhône, promenade au bord de l'Ouvèze... Que faire à Sarrians ce soir ? Idées + pizza livrée.",
   'intro':"Sarrians est un village de la plaine du Comtat Venaissin, à l'ouest de Carpentras. Un village qui vit au rythme des saisons — les vendanges en automne, les marchés en été, et les soirées tranquilles autour d'un bon repas.",
   'sorties':[
     {'t':"La place centrale et ses platanes centenaires",'img':'place.jpg','alt':'Vignobles Côtes-du-Rhône paysage Vaucluse','maps':'Place+de+Sarrians+Vaucluse','cap':'📍 Place de Sarrians',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Place+de+Sarrians+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>place centrale de Sarrians</strong></a>, ombragée de platanes centenaires, est l'épicentre de la vie du village. C'est là qu'on prend un café le matin et qu'on s'attarde au frais le soir.",
      'pizza':"La Reine — simple et bonne, comme cette place."},
     {'t':"Les vins Côtes-du-Rhône de Sarrians",'img':'cave.jpg','alt':'Cave vins Côtes-du-Rhône bouteille','maps':'Cave+vignerons+Sarrians+Vaucluse','cap':'📍 Cave des vignerons de Sarrians',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Cave+vignerons+Sarrians+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>cave coopérative de Sarrians</strong></a> produit des Côtes-du-Rhône Villages appréciés des amateurs. Vente directe, prix cave, accueil chaleureux.",
      'pizza':"La Orientale — épicée et caractérisée, comme les vins du Rhône."},
     {'t':"Promenade au bord de l'Ouvèze",'img':'riviere.jpg','alt':'Dentelles de Montmirail paysage Vaucluse','maps':'Ouvèze+Sarrians+Vaucluse','cap':'📍 Bords de l\'Ouvèze',
      'txt':"À quelques minutes de Sarrians, les <a href=\"https://www.google.com/maps/dir/?api=1&destination=Ouvèze+Sarrians+Vaucluse\" target='_blank' rel='noopener noreferrer'><strong>bords de l'Ouvèze</strong></a> offrent des chemins de promenade paisibles. En soirée, quand la chaleur se dissipe, c'est l'endroit idéal pour une marche.",
      'pizza':"La Tartiflette — pour se réchauffer après la balade."},
   ]},
  {'slug':'caromb','nom':'Caromb','cp':'84330','dept':'Vaucluse',
   'desc':'village médiéval avec son lac et les Dentelles de Montmirail au balcon',
   'meta':"Lac du Paty, village médiéval, vue sur les Dentelles de Montmirail... Que faire à Caromb ce soir ? Idées + pizza livrée.",
   'intro':"Caromb est l'un des villages les mieux gardés du secret vauclusien. Niché entre les Dentelles de Montmirail et le Mont Ventoux, il offre une baignade au lac du Paty en été, un village médiéval intact, et des panoramas qui coupent le souffle.",
   'sorties':[
     {'t':"Le lac du Paty et la baignade",'img':'lac.jpg','alt':'Lac du Paty Caromb Vaucluse baignade','maps':'Lac+du+Paty+Caromb+Vaucluse','cap':'📍 Lac du Paty — Caromb',
      'txt':"Le <a href='https://www.google.com/maps/dir/?api=1&destination=Lac+du+Paty+Caromb+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>lac du Paty</strong></a> est le plan d'eau le plus apprécié du Vaucluse en été. Baignade, vue sur le Ventoux — une journée entière peut s'y passer.",
      'pizza':"La Cochonnaille ou La 4 Fro — pour reconstituer les forces."},
     {'t':"Le village médiéval et l'église Saint-Maurice",'img':'village.jpg','alt':'Porte médiévale village Vaucluse architecture','maps':'Village+médiéval+Caromb+Vaucluse','cap':'📍 Village médiéval de Caromb',
      'txt':"Les ruelles de pierre de <a href='https://www.google.com/maps/dir/?api=1&destination=Village+médiéval+Caromb+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>Caromb</strong></a>, dominées par l'église Saint-Maurice, constituent une promenade de 30 minutes très agréable. Peu fréquenté — c'est tout son charme.",
      'pizza':"La Margharita — authentique, sans chichis."},
     {'t':"Panorama sur les Dentelles de Montmirail",'img':'dentelles.jpg','alt':'Dentelles de Montmirail cascade Lafare','maps':'Dentelles+de+Montmirail+Caromb+Vaucluse','cap':'📍 Dentelles de Montmirail',
      'txt':"Depuis les hauteurs de Caromb, les <a href='https://www.google.com/maps/dir/?api=1&destination=Dentelles+de+Montmirail+Caromb+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>Dentelles de Montmirail</strong></a> se découpent sur le ciel avec une précision chirurgicale. L'un des meilleurs points de vue du secteur, souvent désert.",
      'pizza':"La Saint-Jacques — pour se faire plaisir après une belle journée."},
   ]},
  {'slug':'loriol-du-comtat','nom':'Loriol-du-Comtat','cp':'84870','dept':'Vaucluse',
   'desc':'village médiéval du Comtat Venaissin et son aqueduc des 5 Cantons',
   'meta':"Aqueduc des 5 Cantons, village médiéval, cerisaies du Ventoux... Que faire à Loriol-du-Comtat ? Idées + pizza livrée.",
   'intro':"Loriol-du-Comtat est un petit village du Comtat Venaissin que peu de gens connaissent. Entre un aqueduc historique remarquable et les cerisiers du Ventoux à portée de main, il y a de quoi passer une belle soirée.",
   'sorties':[
     {'t':"L'aqueduc des 5 Cantons",'img':'aqueduc.jpg','alt':'Aqueduc des 5 Cantons Loriol-du-Comtat','maps':'Aqueduc+5+Cantons+Loriol-du-Comtat+Vaucluse','cap':'📍 Aqueduc des 5 Cantons',
      'txt':"L'<a href='https://www.google.com/maps/dir/?api=1&destination=Aqueduc+5+Cantons+Loriol-du-Comtat+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>aqueduc des 5 Cantons</strong></a> est un ouvrage hydraulique du XVIIe siècle. Il traverse le territoire de Loriol dans un paysage de garrigue et de vignes. Une curiosité historique méconnue et impressionnante.",
      'pizza':"La Romaine — pour rester dans l'esprit des grandes constructions."},
     {'t':"Le village médiéval et ses ruelles",'img':'village.jpg','alt':'Village médiéval Comtat Venaissin vue ensemble','maps':'Loriol-du-Comtat+village+Vaucluse','cap':'📍 Centre médiéval de Loriol',
      'txt':"Le cœur de <a href='https://www.google.com/maps/dir/?api=1&destination=Loriol-du-Comtat+village+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>Loriol-du-Comtat</strong></a> a conservé ses ruelles médiévales et sa tour carrée d'époque. Une promenade tranquille dans un village qui vit au rythme provençal.",
      'pizza':"La Reine — classique et rassurante, comme ce village hors du temps."},
     {'t':"Les cerisaies du piémont du Ventoux",'img':'cerisiers.jpg','alt':'Vignes oliviers campagne Vaucluse Provence','maps':'Cerisiers+Ventoux+Vaucluse','cap':'📍 Piémont du Ventoux',
      'txt':"Au printemps, les <a href='https://www.google.com/maps/dir/?api=1&destination=Cerisiers+Ventoux+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>cerisaies du piémont du Ventoux</strong></a> sont en fleurs. Loriol est au cœur de ce paysage blanc et rose qui ne dure que quelques semaines.",
      'pizza':"La Chèvre-Miel — la douceur du miel avec le moelleux du chèvre."},
   ]},
  {'slug':'saint-didier','nom':'Saint-Didier','cp':'84210','dept':'Vaucluse',
   'desc':'village provençal entre Pernes et le plateau de Vaucluse',
   'meta':"Château, fontaine provençale, plateau de Vaucluse... Que faire à Saint-Didier ce soir ? Idées de sorties + pizza livrée.",
   'intro':"Saint-Didier est un village posé entre Pernes-les-Fontaines et les falaises du plateau de Vaucluse. Petit, authentique, il attire les amateurs de Provence tranquille : une fontaine sur la place, un château de caractère, et la forêt du plateau à deux pas.",
   'sorties':[
     {'t':"La place et la fontaine du village",'img':'fontaine.jpg','alt':'Fontaine Saint-Didier Vaucluse','maps':'Place+fontaine+Saint-Didier+Vaucluse','cap':'📍 Fontaine de Saint-Didier',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Place+fontaine+Saint-Didier+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>place avec sa fontaine</strong></a> est le cœur battant de Saint-Didier. Quelques tables de café, des platanes, une fontaine qui chante — le tableau provençal parfait.",
      'pizza':"La Margharita — pour rester dans la simplicité de la place."},
     {'t':"Le Château de Saint-Didier",'img':'chateau.jpg','alt':'Château Provence Vaucluse architecture','maps':'Château+Saint-Didier+Vaucluse','cap':'📍 Château de Saint-Didier',
      'txt':"Le <a href='https://www.google.com/maps/dir/?api=1&destination=Château+Saint-Didier+Vaucluse' target='_blank' rel='noopener noreferrer'><strong>château de Saint-Didier</strong></a> est un bel exemple d'architecture provençale classique entouré de parcs. Sa façade élégante se détache sur les collines du plateau.",
      'pizza':"La Tartufo — une pizza de grand caractère pour un lieu de grand caractère."},
     {'t':"Randonnée vers le plateau de Vaucluse",'img':'plateau.jpg','alt':'Mont Ventoux plateau de Vaucluse panorama','maps':'Plateau+de+Vaucluse+Saint-Didier','cap':'📍 Plateau de Vaucluse',
      'txt':"Saint-Didier est l'un des points d'entrée vers le <a href='https://www.google.com/maps/dir/?api=1&destination=Plateau+de+Vaucluse+Saint-Didier' target='_blank' rel='noopener noreferrer'><strong>plateau de Vaucluse</strong></a>. Les sentiers qui montent vers la forêt offrent une fraîcheur bienvenue en été et des panoramas larges sur la plaine du Comtat.",
      'pizza':"La Cochonnaille — pour recharger les batteries après la montée."},
   ]},
  {'slug':'serres','nom':'Serres','cp':'05700','dept':'Hautes-Alpes',
   'desc':"cité médiévale des Hautes-Alpes, aux portes du lac de Serre-Ponçon",
   'meta':"Citadelle médiévale, lac de Serre-Ponçon, panorama alpin... Que faire à Serres ce soir ? Idées de sorties + pizza livrée.",
   'intro':"Serres est une cité médiévale des Hautes-Alpes perchée sur un éperon rocheux. Elle domine un paysage alpin d'une grandeur rare, et à quelques kilomètres le lac de Serre-Ponçon complète le tableau.",
   'sorties':[
     {'t':"La vieille ville médiévale et la citadelle",'img':'ville.jpg','alt':'Serres vieille ville Hautes-Alpes médiéval','maps':'Vieille+ville+Serres+Hautes-Alpes','cap':'📍 Vieille ville de Serres',
      'txt':"La <a href='https://www.google.com/maps/dir/?api=1&destination=Vieille+ville+Serres+Hautes-Alpes' target='_blank' rel='noopener noreferrer'><strong>vieille ville de Serres</strong></a>, avec ses ruelles voûtées et les restes de sa citadelle, est une plongée directe dans le Moyen Âge alpin. Un ensemble exceptionnel et peu connu.",
      'pizza':"La Romaine — aussi ancienne et solide que les murailles de Serres."},
     {'t':"Le lac de Serre-Ponçon",'img':'lac.jpg','alt':'Lac de Serre-Ponçon Hautes-Alpes barrage','maps':'Lac+de+Serre-Ponçon+Hautes-Alpes','cap':'📍 Lac de Serre-Ponçon',
      'txt':"À quelques kilomètres de Serres, le <a href='https://www.google.com/maps/dir/?api=1&destination=Lac+de+Serre-Ponçon+Hautes-Alpes' target='_blank' rel='noopener noreferrer'><strong>lac de Serre-Ponçon</strong></a> est l'un des plus grands lacs artificiels d'Europe. Baignade, voile, kayak en été — et en toutes saisons une vue sur les sommets alpins enneigés.",
      'pizza':"La 4 Fromages — les fromages des Alpes, en version pizza."},
     {'t':"Panorama sur la vallée du Buëch",'img':'vallee.jpg','alt':'Barrage Serre-Ponçon Hautes-Alpes panorama alpin','maps':'Vallée+du+Buëch+Serres+Hautes-Alpes','cap':'📍 Vallée du Buëch',
      'txt':"Depuis les hauteurs de Serres, la <a href='https://www.google.com/maps/dir/?api=1&destination=Vallée+du+Buëch+Serres+Hautes-Alpes' target='_blank' rel='noopener noreferrer'><strong>vallée du Buëch</strong></a> se déroule vers le sud dans une lumière provençale. Un panorama à 180° sur les pré-Alpes.",
      'pizza':"La Tartiflette — ici dans les Alpes, c'est presque obligatoire."},
   ]},
]

def build(d):
    slug_dir = "que-faire-{}-ce-soir".format(d['slug'])
    url = "{}/blog/{}/".format(SITE, slug_dir)
    nom = d['nom']
    img_folder = "../../livraison-pizza-{}/img".format(d['slug'])

    sorties_html = ''
    for i, s in enumerate(d['sorties']):
        n = i + 1
        img_src = "img/{}".format(s['img'])
        sorties_html += """
    <div class="sortie-card">
      <p class="sortie-num">Idée n°{n}</p>
      <p class="sortie-title">{t}</p>
      <div class="sortie-photo">
        <a href="https://www.google.com/maps/dir/?api=1&destination={maps}" target="_blank" rel="noopener noreferrer">
          <img src="{img_src}" alt="{alt}" loading="lazy">
          <span class="sortie-photo-cap">{cap}</span>
        </a>
      </div>
      <p>{txt}</p>
      <div class="sortie-pizza-tip">🍕 <strong>La pizza conseillée :</strong> {pizza}</div>
    </div>
""".format(n=n, t=s['t'], maps=s['maps'], img_src=img_src, alt=s['alt'], cap=s['cap'], txt=s['txt'], pizza=s['pizza'])

    pub_date = DATES.get(d['slug'], '2026-03-18')
    ld_article = '{{"@context":"https://schema.org","@type":"Article","headline":"Que Faire à {nom} Ce Soir ?","url":"{url}","datePublished":"{date}","dateModified":"{date}","author":{{"@type":"Organization","name":"Pizza Napoli Carpentras"}}}}'.format(nom=nom, url=url, date=pub_date)
    ld_breadcrumb = '{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Accueil","item":"{site}/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"{site}/blog/"}},{{"@type":"ListItem","position":3,"name":"Que Faire à {nom}","item":"{url}"}}]}}'.format(site=SITE, nom=nom, url=url)

    return """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Que Faire à {nom} ? Sorties, Patrimoine + Pizza | Pizza Napoli Carpentras</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="Que Faire à {nom} ? Idées de Sorties + Pizza Livrée">
  <meta property="og:description" content="{meta}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Pizza Napoli Carpentras">
  <meta property="og:image" content="{site}/hero1.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Josefin+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">{ld_bc}</script>
  <script type="application/ld+json">{ld_art}</script>
  <style>{style}
  </style>
</head>
<body>
  <div class="tricolor-bar"><div class="tc-vert"></div><div class="tc-blanc"></div><div class="tc-rouge"></div></div>
  <nav>
    <a href="/" class="nav-logo">Pizza Napoli <span>Carpentras</span></a>
    <a href="tel:0761083608" class="nav-tel">07 61 08 36 08</a>
  </nav>
  <div class="breadcrumb">
    <a href="/">Accueil</a><span>›</span><a href="/blog/">Blog</a><span>›</span>Que faire à {nom} ce soir ?
  </div>
  <div class="article-hero">
    <h1>Que Faire à {nom} ?</h1>
    <p class="hero-sub">{desc_cap} — avec la pizza qu'il faut commander à chaque fois</p>
  </div>
  <div class="article-body">
    <p class="article-meta">Pizza Napoli Carpentras &nbsp;·&nbsp; 3 min de lecture</p>
    <div class="ville-photo">
      <a href="https://www.google.com/maps/dir/?api=1&destination={nom},+{dept},+France" target="_blank" rel="noopener noreferrer">
        <img src="{img_folder}/ville.jpg" alt="{nom}, {dept}" loading="lazy">
        <span class="ville-photo-caption">📍 {nom} ({cp}) — voir l'itinéraire depuis chez vous</span>
      </a>
    </div>
    <p style="font-size:.72rem;color:#aaa;margin-bottom:1.5rem;">Photo : Wikimedia Commons — CC BY-SA</p>
    <p>{intro}</p>
    <h2>Idées de Sorties à {nom}</h2>
{sorties}
    <div class="conseil-box">
      <h3>Pizza Napoli livre à {nom} ({cp})</h3>
      <ul>
        <li><strong>Livraison à {nom} :</strong> 7j/7 de 17h30 à 22h</li>
        <li><strong>À emporter :</strong> <a href="https://www.google.com/maps/dir/?api=1&destination=209+Avenue+Pierre+Sémard,+84200+Carpentras" target="_blank" rel="noopener noreferrer">209 Avenue Pierre Sémard, Carpentras</a></li>
        <li><strong>Commande :</strong> <a href="tel:0761083608">07 61 08 36 08</a></li>
      </ul>
    </div>
    <div class="article-cta">
      <p style="margin-bottom:.8rem;font-size:.9rem;color:rgba(255,255,255,.9);">Quelle que soit votre soirée à {nom}, on s'occupe du repas.</p>
      <a href="tel:0761083608">Commander — 07 61 08 36 08</a>
    </div>
    <h2>À lire aussi</h2>
    <div class="related-articles">
      <div class="related-card">
        <p class="related-card-title">Que Faire à Carpentras ?</p>
        <a href="/blog/que-faire-carpentras-ce-soir/">Lire l'article →</a>
      </div>
      <div class="related-card">
        <p class="related-card-title">Livraison pizza à {nom}</p>
        <a href="/livraison-pizza-{slug}/">Voir les infos →</a>
      </div>
      <div class="related-card">
        <p class="related-card-title">Les 8 Pizzas Incontournables</p>
        <a href="/blog/meilleures-pizzas-carpentras/">Lire l'article →</a>
      </div>
    </div>
  </div>
  <footer>
    <p><strong style="font-family:'Cinzel',serif;">Pizza Napoli Carpentras</strong></p>
    <p><a href="https://www.google.com/maps/dir/?api=1&destination=209+Avenue+Pierre+Sémard,+84200+Carpentras" target="_blank" rel="noopener noreferrer">209 Avenue Pierre Sémard, 84200 Carpentras</a> — <a href="tel:0761083608">07 61 08 36 08</a></p>
    <p>Livraison 7j/7 de 17h30 à 22h — Pizzas dès 6€00</p>
    <p style="margin-top:1rem;"><a href="/">← Retour au site</a> &nbsp;|&nbsp; <a href="/blog/">Blog</a> &nbsp;|&nbsp; <a href="/livraison-pizza-{slug}/">Livraison {nom}</a></p>
    <p style="margin-top:1.2rem;font-size:.75rem;color:rgba(255,255,255,.5);">© 2026 Pizza Napoli Carpentras — Tous droits réservés</p>
  </footer>
  <a href="tel:0761083608" class="float-tel" aria-label="Appeler Pizza Napoli Carpentras">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
  </a>
</body>
</html>""".format(
        nom=nom, meta=d['meta'], url=url, site=SITE, cp=d['cp'], dept=d['dept'],
        desc_cap=d['desc'].capitalize(), intro=d['intro'],
        img_folder=img_folder, sorties=sorties_html, slug=d['slug'],
        style=STYLE, ld_bc=ld_breadcrumb, ld_art=ld_article
    )

for d in TOWNS:
    folder = os.path.join(BASE, "que-faire-{}-ce-soir".format(d['slug']))
    os.makedirs(os.path.join(folder, 'img'), exist_ok=True)
    path = os.path.join(folder, 'index.html')
    html = build(d)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK', d['slug'], len(html), 'chars')

print('\n9 pages generated.')
