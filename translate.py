# Program: Translator
# Name: Gurtej Virdi
# Date: Nov 28, 2020

# Create a dictionary in which the keys and values were swapped
def reverseDictionary(dictionary):
    return {v: k for k, v in dictionary.items()}


# Dictionaries
EtoF_nouns = {'bread': 'pain', 'wine': 'vin', 'friends': 'amis'}
EtoF_adjectives = {'red': 'rouge'}
EtoF_verbs = {'eat': 'mange', 'drink': 'bois', 'love': 'amour'}
EtoF = {'with': 'avec', 'and': 'et',
        'as': 'comme', 'i': 'je', 'his': 'son', 'that': 'que', 'he': 'il', 'was': 'Ã©tait', 'for': 'pour', 'on': 'sur',
        'are': 'sont', 'with': 'avec', 'they': 'ils', 'be': 'Ãªtre', 'at': 'Ã\xa0', 'one': 'un', 'have': 'avoir',
        'this': 'ce', 'from': 'Ã\xa0 partir de', 'by': 'par', 'hot': 'chaud', 'word': 'mot', 'but': 'mais',
        'what': 'que', 'some': 'certains', 'is': 'est', 'it': 'il', 'you': 'vous', 'or': 'ou', 'had': 'eu',
        'the': 'la', 'of': 'du', 'to': 'Ã\xa0', 'and': 'et', 'a': 'un', 'in': 'dans', 'we': 'nous', 'can': 'boÃ®te',
        'out': 'dehors', 'other': 'autre', 'were': 'Ã©taient', 'which': 'qui', 'do': 'faire', 'their': 'leur',
        'time': 'temps', 'if': 'si', 'will': 'volontÃ©', 'how': 'comment', 'said': 'dit', 'an': 'un', 'each': 'chaque',
        'tell': 'dire', 'does': 'ne', 'set': 'ensemble', 'three': 'trois', 'want': 'vouloir', 'air': 'air',
        'well': 'bien', 'also': 'aussi', 'play': 'jouer', 'small': 'petit', 'end': 'fin', 'put': 'mettre',
        'home': 'maison', 'read': 'lire', 'hand': 'main', 'port': 'port', 'large': 'grand', 'spell': 'Ã©peler',
        'add': 'ajouter', 'even': 'mÃªme', 'land': 'terre', 'here': 'ici', 'must': 'il faut', 'big': 'grand',
        'high': 'haut', 'such': 'tel', 'follow': 'suivre', 'act': 'acte', 'why': 'pourquoi', 'ask': 'interroger',
        'men': 'hommes', 'change': 'changement', 'went': 'est allÃ©', 'light': 'lumiÃ¨re', 'kind': 'genre',
        'off': 'de', 'need': 'besoin', 'house': 'maison', 'picture': 'image', 'try': 'essayer', 'us': 'nous',
        'again': 'encore', 'animal': 'animal', 'point': 'point', 'mother': 'mÃ¨re', 'world': 'monde',
        'near': 'prÃ¨s de', 'build': 'construire', 'self': 'soi', 'earth': 'terre', 'father': 'pÃ¨re', 'any': 'tout',
        'new': 'nouveau', 'work': 'travail', 'part': 'partie', 'take': 'prendre', 'get': 'obtenir', 'place': 'lieu',
        'made': 'fabriquÃ©', 'live': 'vivre', 'where': 'oÃ¹', 'after': 'aprÃ¨s', 'back': 'arriÃ¨re', 'little': 'peu',
        'only': 'seulement', 'round': 'tour', 'man': 'homme', 'year': 'annÃ©e', 'came': 'est venu', 'show': 'montrer',
        'every': 'tous', 'good': 'bon', 'me': 'moi', 'give': 'donner', 'our': 'notre', 'under': 'sous', 'name': 'nom',
        'very': 'trÃ¨s', 'through': 'par', 'just': 'juste', 'form': 'forme', 'sentence': 'phrase', 'great': 'grand',
        'think': 'penser', 'say': 'dire', 'help': 'aider', 'low': 'faible', 'line': 'ligne', 'differ': 'diffÃ©rer',
        'turn': 'tour', 'cause': 'la cause', 'much': 'beaucoup', 'mean': 'signifier', 'before': 'avant',
        'move': 'dÃ©mÃ©nagement', 'right': 'droit', 'boy': 'garÃ§on', 'old': 'vieux', 'too': 'trop', 'same': 'mÃªme',
        'she': 'elle', 'all': 'tous', 'there': 'lÃ\xa0', 'when': 'quand', 'up': 'jusquâ€™Ã\xa0', 'use': 'utiliser',
        'your': 'votre', 'way': 'maniÃ¨re', 'about': 'sur', 'many': 'beaucoup', 'then': 'puis', 'them': 'les',
        'write': 'Ã©crire', 'would': 'voudrais', 'like': 'comme', 'so': 'si', 'these': 'ces', 'her': 'son',
        'long': 'long', 'make': 'faire', 'thing': 'chose', 'see': 'voir', 'him': 'lui', 'two': 'deux', 'has': 'a',
        'look': 'regarder', 'more': 'plus', 'day': 'jour', 'could': 'pourrait', 'go': 'aller', 'come': 'venir',
        'did': 'fait', 'number': 'nombre', 'sound': 'son', 'no': 'aucun', 'most': 'plus', 'people': 'personnes',
        'my': 'ma', 'over': 'sur', 'know': 'savoir', 'water': 'eau', 'than': 'que', 'call': 'appel',
        'first': 'premiÃ¨re', 'who': 'qui', 'may': 'peut', 'down': 'vers le bas', 'side': 'cÃ´tÃ©', 'been': 'Ã©tÃ©',
        'now': 'maintenant', 'find': 'trouver', 'head': 'tÃªte', 'stand': 'supporter', 'own': 'propre', 'page': 'page',
        'should': 'devrait', 'country': 'pays', 'found': 'trouvÃ©', 'answer': 'rÃ©ponse', 'school': 'Ã©cole',
        'grow': 'croÃ®tre', 'study': 'Ã©tude', 'still': 'encore', 'learn': 'apprendre', 'plant': 'usine',
        'cover': 'couvercle', 'food': 'nourriture', 'sun': 'soleil', 'four': 'quatre', 'between': 'entre',
        'state': 'Ã©tat', 'keep': 'garder', 'eye': 'Å“il', 'never': 'jamais', 'last': 'dernier', 'let': 'laisser',
        'thought': 'pensÃ©e', 'city': 'ville', 'tree': 'arbre', 'cross': 'traverser', 'farm': 'ferme', 'hard': 'dur',
        'start': 'dÃ©but', 'might': 'puissance', 'story': 'histoire', 'saw': 'scie', 'far': 'loin', 'sea': 'mer',
        'draw': 'tirer', 'left': 'gauche', 'late': 'tard', 'run': 'courir', 'donâ€™t': 'needs a context',
        'while': 'tandis que', 'press': 'presse', 'close': 'proche', 'night': 'nuit', 'real': 'rÃ©el', 'life': 'vie',
        'few': 'peu', 'north': 'nord', 'book': 'livre', 'carry': 'porter', 'took': 'a pris', 'science': 'science',
        'eat': 'manger', 'room': 'chambre', 'friend': 'ami', 'began': 'a commencÃ©', 'idea': 'idÃ©e',
        'fish': 'poisson', 'mountain': 'montagne', 'stop': 'ArrÃªtez', 'once': 'une fois', 'base': 'base',
        'hear': 'entendre', 'horse': 'cheval', 'cut': 'coupe', 'sure': 'sÃ»r', 'watch': 'regarder', 'color': 'couleur',
        'face': 'face', 'wood': 'bois', 'main': 'principal', 'open': 'ouvert', 'seem': 'paraÃ®tre',
        'together': 'ensemble', 'next': 'suivant', 'white': 'blanc', 'children': 'enfants', 'begin': 'commencer',
        'got': 'eu', 'walk': 'marcher', 'example': 'exemple', 'ease': 'facilitÃ©', 'paper': 'papier',
        'group': 'groupe', 'always': 'toujours', 'music': 'musique', 'those': 'ceux', 'both': 'tous les deux',
        'mark': 'marque', 'often': 'souvent', 'letter': 'lettre', 'until': 'jusquâ€™Ã\xa0 ce que', 'mile': 'mile',
        'river': 'riviÃ¨re', 'car': 'voiture', 'feet': 'pieds', 'care': 'soins', 'second': 'deuxiÃ¨me',
        'enough': 'assez', 'plain': 'plaine', 'girl': 'fille', 'usual': 'habituel', 'young': 'jeune', 'ready': 'prÃªt',
        'above': 'au-dessus', 'ever': 'jamais', 'red': 'rouge', 'list': 'liste', 'though': 'bien que',
        'feel': 'sentir', 'talk': 'parler', 'bird': 'oiseau', 'soon': 'bientÃ´t', 'body': 'corps', 'dog': 'chien',
        'family': 'famille', 'direct': 'direct', 'pose': 'pose', 'leave': 'laisser', 'song': 'chanson',
        'measure': 'mesurer', 'door': 'porte', 'product': 'produit', 'black': 'noir', 'short': 'court',
        'numeral': 'chiffre', 'class': 'classe', 'wind': 'vent', 'question': 'question', 'happen': 'arriver',
        'complete': 'complÃ¨te', 'ship': 'navire', 'area': 'zone', 'half': 'moitiÃ©', 'rock': 'rock', 'order': 'ordre',
        'fire': 'feu', 'south': 'sud', 'problem': 'problÃ¨me', 'piece': 'piÃ¨ce', 'told': 'dit', 'knew': 'savait',
        'pass': 'passer', 'since': 'depuis', 'top': 'haut', 'whole': 'ensemble', 'king': 'roi', 'street': 'rue',
        'inch': 'pouce', 'multiply': 'multiplier', 'nothing': 'rien', 'course': 'cours', 'stay': 'rester',
        'wheel': 'roue', 'full': 'plein', 'force': 'force', 'blue': 'bleu', 'object': 'objet', 'decide': 'dÃ©cider',
        'surface': 'surface', 'deep': 'profond', 'moon': 'lune', 'island': 'Ã®le', 'foot': 'pied',
        'system': 'systÃ¨me', 'busy': 'occupÃ©', 'test': 'test', 'record': 'record', 'boat': 'bateau',
        'common': 'commun', 'gold': 'or', 'possible': 'possible', 'plane': 'plan', 'stead': 'place', 'dry': 'sec',
        'wonder': 'se demander', 'laugh': 'rire', 'thousand': 'mille', 'ago': 'il ya', 'ran': 'ran',
        'check': 'vÃ©rifier', 'game': 'jeu', 'shape': 'forme', 'equate': 'assimiler', 'miss': 'manquer',
        'brought': 'apportÃ©', 'heat': 'chaleur', 'snow': 'neige', 'tire': 'pneu', 'bring': 'apporter', 'yes': 'oui',
        'distant': 'lointain', 'fill': 'remplir', 'east': 'est', 'paint': 'peindre', 'language': 'langue',
        'among': 'entre', 'unit': 'unitÃ©', 'power': 'puissance', 'town': 'ville', 'fine': 'fin', 'certain': 'certain',
        'fly': 'voler', 'fall': 'tomber', 'lead': 'conduire', 'cry': 'cri', 'dark': 'sombre', 'machine': 'machine',
        'note': 'Note', 'wait': 'patienter', 'plan': 'plan', 'figure': 'figure', 'star': 'Ã©toile', 'box': 'boÃ®te',
        'noun': 'nom', 'field': 'domaine', 'rest': 'reste', 'correct': 'correct', 'able': 'capable', 'pound': 'livre',
        'done': 'TerminÃ©', 'beauty': 'beautÃ©', 'drive': 'entraÃ®nement', 'stood': 'rÃ©sistÃ©', 'contain': 'contenir',
        'front': 'avant', 'teach': 'enseigner', 'week': 'semaine', 'final': 'finale', 'gave': 'donnÃ©',
        'green': 'vert', 'oh': 'oh', 'quick': 'rapide', 'develop': 'dÃ©velopper', 'ocean': 'ocÃ©an', 'warm': 'chaud',
        'free': 'gratuit', 'minute': 'minute', 'strong': 'fort', 'special': 'spÃ©cial', 'mind': 'esprit',
        'behind': 'derriÃ¨re', 'clear': 'clair', 'tail': 'queue', 'produce': 'produire', 'fact': 'fait',
        'space': 'espace', 'heard': 'entendu', 'best': 'meilleur', 'hour': 'heure', 'better': 'mieux', 'TRUE': 'vrai',
        'during': 'pendant', 'hundred': 'cent', 'five': 'cinq', 'remember': 'rappeler', 'step': 'Ã©tape',
        'early': 'tÃ´t', 'hold': 'tenir', 'west': 'ouest', 'ground': 'sol', 'interest': 'intÃ©rÃªt',
        'reach': 'atteindre', 'fast': 'rapide', 'verb': 'verbe', 'sing': 'chanter', 'listen': 'Ã©couter', 'six': 'six',
        'table': 'table', 'travel': 'Voyage', 'less': 'moins', 'morning': 'matin', 'ten': 'dix', 'simple': 'simple',
        'several': 'plusieurs', 'vowel': 'voyelle', 'toward': 'vers', 'war': 'guerre', 'lay': 'poser',
        'against': 'contre', 'pattern': 'modÃ¨le', 'slow': 'lent', 'center': 'centre', 'love': 'amour',
        'person': 'personne', 'money': 'argent', 'serve': 'servir', 'appear': 'apparaÃ®tre', 'road': 'route',
        'map': 'carte', 'rain': 'pluie', 'rule': 'rÃ¨gle', 'govern': 'gouverner', 'pull': 'tirer', 'cold': 'froid',
        'notice': 'avis', 'voice': 'voix', 'energy': 'Ã©nergie', 'hunt': 'chasse', 'probable': 'probable',
        'bed': 'lit', 'brother': 'frÃ¨re', 'egg': 'Å“uf', 'ride': 'tour', 'cell': 'cellule', 'believe': 'croire',
        'perhaps': 'peut-Ãªtre', 'pick': 'choisir', 'sudden': 'soudain', 'count': 'compter', 'square': 'carrÃ©',
        'reason': 'raison', 'length': 'longueur', 'represent': 'reprÃ©senter', 'art': 'art', 'subject': 'sujet',
        'region': 'rÃ©gion', 'size': 'taille', 'vary': 'varier', 'settle': 'rÃ©gler', 'speak': 'parler',
        'weight': 'poids', 'general': 'gÃ©nÃ©ral', 'ice': 'glace', 'matter': 'question', 'circle': 'cercle',
        'pair': 'paire', 'include': 'inclure', 'divide': 'fracture', 'syllable': 'syllabe', 'felt': 'feutre',
        'grand': 'grandiose', 'ball': 'balle', 'yet': 'encore', 'wave': 'vague', 'drop': 'tomber', 'heart': 'cÅ“ur',
        'am': 'h', 'present': 'prÃ©sent', 'heavy': 'lourd', 'dance': 'danse', 'engine': 'moteur',
        'position': 'position', 'arm': 'bras', 'wide': 'large', 'sail': 'voile', 'material': 'matÃ©riel',
        'fraction': 'fraction', 'forest': 'forÃªt', 'sit': 'sâ€™asseoir', 'race': 'course', 'window': 'fenÃªtre',
        'store': 'magasin', 'summer': 'Ã©tÃ©', 'train': 'train', 'sleep': 'sommeil', 'prove': 'prouver',
        'lone': 'seul', 'leg': 'jambe', 'exercise': 'exercice', 'wall': 'mur', 'catch': 'capture', 'mount': 'monture',
        'wish': 'souhaiter', 'sky': 'ciel', 'board': 'conseil', 'joy': 'joie', 'winter': 'hiver', 'sat': 'sat',
        'written': 'Ã©crit', 'wild': 'sauvage', 'instrument': 'instrument', 'kept': 'conservÃ©', 'glass': 'verre',
        'grass': 'herbe', 'cow': 'vache', 'job': 'emploi', 'edge': 'bord', 'sign': 'signe', 'visit': 'visite',
        'past': 'passÃ©', 'soft': 'doux', 'fun': 'amusement', 'bright': 'clair', 'gas': 'gaz', 'weather': 'temps',
        'month': 'mois', 'million': 'million', 'bear': 'porter', 'finish': 'finition', 'happy': 'heureux',
        'hope': 'espoir', 'flower': 'fleur', 'clothe': 'vÃªtir', 'strange': 'Ã©trange', 'gone': 'disparu',
        'trade': 'commerce', 'melody': 'mÃ©lodie', 'trip': 'voyage', 'office': 'bureau', 'receive': 'recevoir',
        'row': 'rangÃ©e', 'mouth': 'bouche', 'exact': 'exact', 'symbol': 'symbole', 'die': 'mourir', 'least': 'moins',
        'trouble': 'difficultÃ©', 'shout': 'cri', 'except': 'sauf', 'wrote': 'Ã©crit', 'seed': 'semence',
        'tone': 'ton', 'join': 'joindre', 'suggest': 'suggÃ©rer', 'clean': 'propre', 'break': 'pause', 'lady': 'dame',
        'yard': 'cour', 'rise': 'augmenter', 'bad': 'mauvais', 'blow': 'coup', 'oil': 'huile', 'blood': 'sang',
        'touch': 'toucher', 'grew': 'a augmentÃ©', 'cent': 'cent', 'mix': 'mÃ©langer', 'team': 'Ã©quipe',
        'wire': 'fil', 'cost': 'coÃ»t', 'lost': 'perdu', 'brown': 'brun', 'wear': 'porter', 'garden': 'jardin',
        'equal': 'Ã©gal', 'sent': 'expÃ©diÃ©', 'choose': 'choisir', 'fell': 'est tombÃ©', 'fit': 'sâ€™adapter',
        'flow': 'dÃ©bit', 'fair': 'juste', 'bank': 'banque', 'collect': 'recueillir', 'save': 'sauver',
        'control': 'contrÃ´le', 'decimal': 'dÃ©cimal', 'ear': 'oreille', 'else': 'autre', 'quite': 'tout Ã\xa0 fait',
        'broke': 'cassÃ©', 'case': 'cas', 'middle': 'milieu', 'kill': 'tuer', 'son': 'fils', 'lake': 'lac',
        'moment': 'moment', 'scale': 'Ã©chelle', 'loud': 'fort', 'spring': 'printemps', 'observe': 'observer',
        'child': 'enfant', 'straight': 'droit', 'consonant': 'consonne', 'nation': 'nation',
        'dictionary': 'dictionnaire', 'milk': 'lait', 'speed': 'vitesse', 'method': 'mÃ©thode', 'organ': 'organe',
        'pay': 'payer', 'age': 'Ã¢ge', 'section': 'section', 'dress': 'robe', 'cloud': 'nuage', 'surprise': 'surprise',
        'quiet': 'calme', 'stone': 'pierre', 'tiny': 'minuscule', 'climb': 'montÃ©e', 'cool': 'frais',
        'design': 'conception', 'poor': 'pauvres', 'lot': 'lot', 'experiment': 'expÃ©rience', 'bottom': 'bas',
        'key': 'clÃ©', 'iron': 'fer', 'single': 'unique', 'stick': 'bÃ¢ton', 'flat': 'plat', 'twenty': 'vingt',
        'skin': 'peau', 'smile': 'sourire', 'crease': 'pli', 'hole': 'trou', 'jump': 'sauter', 'baby': 'bÃ©bÃ©',
        'eight': 'huit', 'village': 'village', 'meet': 'se rencontrent', 'root': 'racine', 'buy': 'acheter',
        'raise': 'augmenter', 'solve': 'rÃ©soudre', 'metal': 'mÃ©tal', 'whether': 'si', 'push': 'pousser',
        'seven': 'sept', 'paragraph': 'paragraphe', 'third': 'troisiÃ¨me', 'shall': 'doit', 'held': 'en attente',
        'hair': 'cheveux', 'describe': 'dÃ©crire', 'cook': 'cuisinier', 'floor': 'Ã©tage', 'either': 'chaque',
        'result': 'rÃ©sultat', 'burn': 'brÃ»ler', 'hill': 'colline', 'safe': 'coffre-fort', 'cat': 'chat',
        'century': 'siÃ¨cle', 'consider': 'envisager', 'type': 'type', 'law': 'droit', 'bit': 'peu', 'coast': 'cÃ´te',
        'copy': 'copie', 'phrase': 'phrase', 'silent': 'silencieux', 'tall': 'haut', 'sand': 'sable', 'soil': 'sol',
        'roll': 'rouleau', 'temperature': 'tempÃ©rature', 'finger': 'doigt', 'industry': 'industrie',
        'value': 'valeur', 'fight': 'lutte', 'lie': 'mensonge', 'beat': 'battre', 'excite': 'exciter',
        'natural': 'naturel', 'view': 'vue', 'sense': 'sens', 'capital': 'capital', 'wonâ€™t': 'ne sera pas',
        'chair': 'chaise', 'danger': 'danger', 'fruit': 'fruit', 'rich': 'riche', 'thick': 'Ã©pais',
        'soldier': 'soldat', 'process': 'processus', 'operate': 'fonctionner', 'practice': 'pratique',
        'separate': 'sÃ©parÃ©', 'difficult': 'difficile', 'doctor': 'mÃ©decin', 'please': 'sâ€™il vous plaÃ®t',
        'protect': 'protÃ©ger', 'noon': 'midi', 'crop': 'rÃ©colte', 'modern': 'moderne', 'element': 'Ã©lÃ©ment',
        'hit': 'frapper', 'student': 'Ã©tudiant', 'corner': 'coin', 'party': 'partie', 'supply': 'alimentation',
        'whose': 'dont', 'locate': 'localiser', 'ring': 'anneau', 'character': 'caractÃ¨re', 'insect': 'insecte',
        'caught': 'pris', 'period': 'pÃ©riode', 'indicate': 'indiquer', 'radio': 'radio', 'spoke': 'rayon',
        'atom': 'atome', 'human': 'humain', 'history': 'histoire', 'effect': 'effet', 'electric': 'Ã©lectrique',
        'expect': 'attendre', 'bone': 'os', 'rail': 'rail', 'imagine': 'imaginer', 'provide': 'fournir',
        'agree': 'se mettre dâ€™accord', 'thus': 'ainsi', 'gentle': 'doux', 'woman': 'femme', 'captain': 'capitaine',
        'guess': 'deviner', 'necessary': 'nÃ©cessaire', 'sharp': 'net', 'wing': 'aile', 'create': 'crÃ©er',
        'neighbor': 'voisin', 'wash': 'lavage', 'bat': 'chauve-souris', 'rather': 'plutÃ´t', 'crowd': 'foule',
        'corn': 'blÃ©', 'compare': 'comparer', 'poem': 'poÃ¨me', 'string': 'chaÃ®ne', 'bell': 'cloche',
        'depend': 'dÃ©pendre', 'meat': 'viande', 'rub': 'rub', 'tube': 'tube', 'famous': 'cÃ©lÃ¨bre',
        'dollar': 'dollar', 'stream': 'courant', 'fear': 'peur', 'sight': 'vue', 'thin': 'mince',
        'triangle': 'triangle', 'planet': 'planÃ¨te', 'hurry': 'se dÃ©pÃªcher', 'chief': 'chef', 'colony': 'colonie',
        'clock': 'horloge', 'mine': 'mine', 'tie': 'lien', 'enter': 'entrer', 'major': 'majeur', 'fresh': 'frais',
        'search': 'recherche', 'send': 'envoyer', 'yellow': 'jaune', 'gun': 'pistolet', 'allow': 'permettre',
        'print': 'impression', 'dead': 'mort', 'spot': 'place', 'desert': 'dÃ©sert', 'suit': 'costume',
        'current': 'courant', 'lift': 'ascenseur', 'rose': 'rose', 'arrive': 'arriver', 'master': 'maÃ®tre',
        'track': 'piste', 'parent': 'mÃ¨re', 'shore': 'rivage', 'division': 'division', 'sheet': 'feuille',
        'substance': 'substance', 'favor': 'favoriser', 'connect': 'relier', 'post': 'poste', 'spend': 'passer',
        'chord': 'corde', 'fat': 'graisse', 'glad': 'heureux', 'original': 'original', 'share': 'part',
        'station': 'station', 'dad': 'papa', 'bread': 'pain', 'charge': 'charger', 'proper': 'propre', 'bar': 'bar',
        'offer': 'proposition', 'segment': 'segment', 'slave': 'esclave', 'duck': 'canard', 'instant': 'instant',
        'market': 'marchÃ©', 'degree': 'degrÃ©', 'populate': 'peupler', 'chick': 'poussin', 'dear': 'cher',
        'enemy': 'ennemi', 'reply': 'rÃ©pondre', 'drink': 'boisson', 'occur': 'se produire', 'support': 'support',
        'speech': 'discours', 'nature': 'nature', 'range': 'gamme', 'steam': 'vapeur', 'motion': 'mouvement',
        'path': 'chemin', 'liquid': 'liquide', 'log': 'enregistrer', 'meant': 'signifiait', 'quotient': 'quotient',
        'teeth': 'dents', 'shell': 'coquille', 'neck': 'cou', 'oxygen': 'oxygÃ¨ne', 'sugar': 'sucre',
        'death': 'dÃ©cÃ¨s', 'pretty': 'assez', 'skill': 'compÃ©tence', 'women': 'femmes', 'season': 'saison',
        'solution': 'solution', 'magnet': 'aimant', 'silver': 'argent', 'thank': 'merci', 'branch': 'branche',
        'match': 'rencontre', 'suffix': 'suffixe', 'especially': 'particuliÃ¨rement', 'fig': 'figue', 'afraid': 'peur',
        'huge': 'Ã©norme', 'sister': 'sÅ“ur', 'steel': 'acier', 'discuss': 'discuter', 'forward': 'avant',
        'similar': 'similaire', 'guide': 'guider', 'experience': 'expÃ©rience', 'score': 'score', 'apple': 'pomme',
        'bought': 'achetÃ©', 'led': 'LED', 'pitch': 'pas', 'coat': 'manteau', 'mass': 'masse', 'card': 'carte',
        'band': 'bande', 'rope': 'corde', 'slip': 'glissement', 'win': 'gagner', 'dream': 'rÃªver',
        'evening': 'soirÃ©e', 'condition': 'condition', 'feed': 'alimentation', 'tool': 'outil', 'total': 'total',
        'basic': 'de base', 'smell': 'odeur', 'valley': 'vallÃ©e', 'nor': 'ni', 'double': 'double', 'seat': 'siÃ¨ge',
        'continue': 'continuer', 'block': 'bloc', 'chart': 'graphique', 'hat': 'chapeau', 'sell': 'vendre',
        'success': 'succÃ¨s', 'company': 'entreprise', 'subtract': 'soustraire', 'event': 'Ã©vÃ©nement',
        'particular': 'particulier', 'deal': 'accord', 'swim': 'baignade', 'term': 'terme', 'opposite': 'opposÃ©',
        'wife': 'femme', 'shoe': 'chaussure', 'shoulder': 'Ã©paule', 'spread': 'propagation', 'arrange': 'organiser',
        'camp': 'camp', 'invent': 'inventer', 'cotton': 'coton', 'born': 'nÃ©', 'determine': 'dÃ©terminer',
        'quart': 'litre', 'nine': 'neuf', 'truck': 'camion', 'noise': 'bruit', 'level': 'niveau', 'chance': 'chance',
        'gather': 'recueillir', 'shop': 'boutique', 'stretch': 'tronÃ§on', 'throw': 'jeter', 'shine': 'Ã©clat',
        'property': 'propriÃ©tÃ©', 'column': 'colonne', 'molecule': 'molÃ©cule', 'select': 'sÃ©lectionner',
        'wrong': 'mal', 'gray': 'gris', 'repeat': 'rÃ©pÃ©tition', 'require': 'exiger', 'broad': 'large',
        'prepare': 'prÃ©parer', 'salt': 'sel', 'nose': 'nez', 'plural': 'pluriel', 'anger': 'colÃ¨re',
        'claim': 'revendication', 'continent': 'continent'}
EtoF.update(dict(list(EtoF_verbs.items()) + list(EtoF_adjectives.items()) + list(EtoF_nouns.items())))
FtoE_nouns = reverseDictionary(EtoF_nouns)
FtoE_adjectives = reverseDictionary(EtoF_adjectives)
FtoE_verbs = reverseDictionary(EtoF_verbs)
FtoE = reverseDictionary(EtoF)
dicts = {'English to French': EtoF, 'French to English': FtoE}


# Translate word
def translateWord(word, dictionary):
    if word.lower() in dictionary.keys():
        if word.lower() == 'je':
            return dictionary[word.lower()].capitalize()
        else:
            return dictionary[word.lower()]
    elif word != '':
        return '"' + word + '"'
    return word


# Fix j'
def fix_j_apostrophe(s, d):
    if d == EtoF:
        if ',' in s:
            return fix_j_apostrophe(s.split(',', maxsplit=1)[0], EtoF) + ', ' + fix_j_apostrophe(
                s.split(',', maxsplit=1)[1], EtoF)
        elif '.' in s:
            return fix_j_apostrophe(s.split('.', maxsplit=1)[0], EtoF) + '. ' + fix_j_apostrophe(
                s.split('.', maxsplit=1)[1], EtoF)
        elif ';' in s:
            return fix_j_apostrophe(s.split(';', maxsplit=1)[0], EtoF) + '; ' + fix_j_apostrophe(
                s.split(';', maxsplit=1)[1], EtoF)
        elif '!' in s:
            return fix_j_apostrophe(s.split('!', maxsplit=1)[0], EtoF) + '! ' + fix_j_apostrophe(
                s.split('!', maxsplit=1)[1], EtoF)
        elif '?' in s:
            return fix_j_apostrophe(s.split('?', maxsplit=1)[0], EtoF) + '? ' + fix_j_apostrophe(
                s.split('?', maxsplit=1)[1], EtoF)
        else:
            s = s.split()
            for i in range(len(s) - 1):
                if s[i].lower() == 'je' and s[i + 1].lower()[0] in 'aeiou' and s[i + 1].lower() in FtoE_verbs.keys():
                    s = s[:i] + ['j\'' + s[i + 1]] + s[i + 2:]
            return ' '.join(s)
    elif d == FtoE:
        if 'j\'' in s:
            s = s.replace('j\'', 'je ')
        if 'J\'' in s:
            s = s.replace('J\'', 'je ')
        return s


# Fix adjacent words
def fix_adjacent_words(s, d):
    if d == FtoE:
        if ',' in s:
            return fix_adjacent_words(s.split(',', maxsplit=1)[0], FtoE) + ', ' + fix_adjacent_words(
                s.split(',', maxsplit=1)[1], FtoE)
        elif '.' in s:
            return fix_adjacent_words(s.split('.', maxsplit=1)[0], FtoE) + '. ' + fix_adjacent_words(
                s.split('.', maxsplit=1)[1], FtoE)
        elif ';' in s:
            return fix_adjacent_words(s.split(';', maxsplit=1)[0], FtoE) + '; ' + fix_adjacent_words(
                s.split(';', maxsplit=1)[1], FtoE)
        elif '!' in s:
            return fix_adjacent_words(s.split('!', maxsplit=1)[0], FtoE) + '! ' + fix_adjacent_words(
                s.split('!', maxsplit=1)[1], FtoE)
        elif '?' in s:
            return fix_adjacent_words(s.split('?', maxsplit=1)[0], FtoE) + '? ' + fix_adjacent_words(
                s.split('?', maxsplit=1)[1], FtoE)
        else:
            s = s.split()
            for i in range(len(s) - 1):
                if s[i].lower() in EtoF_nouns.keys() and s[i + 1].lower() in EtoF_adjectives.keys():
                    s[i], s[i + 1] = s[i + 1], s[i]
            return ' '.join(s)
    elif d == EtoF:
        if ',' in s:
            return fix_adjacent_words(s.split(',', maxsplit=1)[0], EtoF) + ', ' + fix_adjacent_words(
                s.split(',', maxsplit=1)[1], EtoF)
        elif '.' in s:
            return fix_adjacent_words(s.split('.', maxsplit=1)[0], EtoF) + '. ' + fix_adjacent_words(
                s.split('.', maxsplit=1)[1], EtoF)
        elif ';' in s:
            return fix_adjacent_words(s.split(';', maxsplit=1)[0], EtoF) + '; ' + fix_adjacent_words(
                s.split(';', maxsplit=1)[1], EtoF)
        elif '!' in s:
            return fix_adjacent_words(s.split('!', maxsplit=1)[0], EtoF) + '! ' + fix_adjacent_words(
                s.split('!', maxsplit=1)[1], EtoF)
        elif '?' in s:
            return fix_adjacent_words(s.split('?', maxsplit=1)[0], EtoF) + '? ' + fix_adjacent_words(
                s.split('?', maxsplit=1)[1], EtoF)
        else:
            s = s.split()
            for i in range(len(s) - 1):
                if s[i].lower() in FtoE_adjectives.keys() and s[i + 1].lower() in FtoE_nouns.keys():
                    s[i], s[i + 1] = s[i + 1], s[i]
            return ' '.join(s)


# Capitalize first word in sentence
def capitalize_str(s):
    if '.' in s:
        return capitalize_str(s.split('.', maxsplit=1)[0]) + '. ' + capitalize_str(s.split('.', maxsplit=1)[1])
    elif '!' in s:
        return capitalize_str(s.split('!', maxsplit=1)[0]) + '! ' + capitalize_str(s.split('!', maxsplit=1)[1])
    elif '?' in s:
        return capitalize_str(s.split('?', maxsplit=1)[0]) + '? ' + capitalize_str(s.split('?', maxsplit=1)[1])
    else:
        s = s.split()
        return ' '.join([s[i].capitalize().strip() if i == 0 else s[i].strip() for i in range(len(s))])


# Translate sentences
def translate(phrase, dicts, direction):
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÂÇÆÉÈÊËÏÎÔŒÙÛÜŸ'
    LCletters = 'abcdefghijklmnopqrstuvwxyzàâçæéèêëïîôœùûüÿ'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    if dictionary == FtoE:
        phrase = fix_j_apostrophe(phrase, dictionary)
    translation = ''
    word = ''
    for character in phrase:
        if character in letters:
            word = word + character
        else:
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary)
    if dictionary == EtoF:
        translation = fix_j_apostrophe(translation, dictionary)
    translation = fix_adjacent_words(translation, dictionary)
    translation = capitalize_str(translation)
    return translation


# Ask to run again
def ask_again():
    return input('Would you like to run this program again? ')[0].lower() == 'y'


# Main
if __name__ == '__main__':
    print('Python Translator')
    print('Vocabulary of', len(EtoF), 'words')
    print('Domain - most commonly used English words')
    while True:
        print('Please select operation -')
        print('1. English to French')
        print('2. French to English')
        select = int(input('Select operations form 1, 2: '))
        if select == 1:
            print('--------------------------------------')
            user_input = input('Input: ')
            output = translate(user_input, dicts, 'English to French')
            print('Output:', output)
            f = open("output.txt", "a")
            f.write('Input: ' + user_input + '\n')
            f.write('Output: ' + output + '\n')
            f.close()
            print('--------------------------------------')
        elif select == 2:
            print('--------------------------------------')
            user_input = input('Input: ')
            output = translate(user_input, dicts, 'French to English')
            print('Output:', output)
            f = open("output.txt", "a")
            f.write('Input: ' + user_input + '\n')
            f.write('Output: ' + output + '\n')
            f.close()
            print('--------------------------------------')
        else:
            print('Invalid input')
        if not ask_again():
            exit()
