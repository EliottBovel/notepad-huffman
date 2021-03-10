from hufflib import codage


def encodage (texte, dico):
    """Encode la phrase de départ à partir de la bibliothèque de code"""
    dico = codage.getCodage(dico)
    code = ""
    for i in range(len(texte)): #Récupération longueur du texte pour traduire chaque lettre
        if texte[i] in dico: #vérif lettre encodé
            code_l = dico[texte[i]]
            code += code_l
        else :
            return "Erreur, lettre non encodé"
    return code