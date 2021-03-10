from collections import Counter

def compt_occ(texte):
    l=[]
    occurence = Counter(texte)
    for (key, value) in occurence.items():
        t=(key,value)
        l.append(t)
    return l

def tri(liste):
    l_tri=sorted(liste, key=lambda x: x[1])
    return l_tri

def getDoubles(texte):
    return tri(compt_occ(texte))