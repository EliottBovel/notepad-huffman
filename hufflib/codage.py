def getCodage(arbre):
    """
    Fonction qui retourne un dictionnaire
    qui a pour clés : les lettres
    et pour valeurs : leurs codage en binaire
    :Parametre:
    arbre : arbre -> arbre de compression codé en POO
    :Return:
    codes : dict -> contient le codage de chaques lettres
    """
    #INITIALISATION
    codes = dict()
    codage = ""

    #Appel de la fonction parcours
    parcours(arbre, codage, codes)
    #print("codes : ", codes)

    for k,v in codes.items():
        if v == "":
            codes[k] = "0"

    return codes

    

def parcours(arbre, codage, codes):
    """
    Fonction qui parcours l'arbre compressé et qui permet
    de retourner le codage d'une lettre dans l'arbre
    :Parameters:
    arbre : arbre -> arbre de compression codé en POO
    code : list -> codage d'une lettre de l'arbre
    lettre : str -> lettre à codé
    :Return:
    code : str -> Codage de la lettre
    """
    if arbre:
        #Condition pour ajouter un élément dans le dictionnaire
        if arbre.left == None and arbre.right == None:
            if arbre.car != None:
                #Ajout d'un élélment dans le dictionnaire
                codes[arbre.car] = codage

        if arbre.left != None:
            parcours(arbre.left, codage + '0', codes)

        if arbre.right != None:
            parcours(arbre.right, codage + '1', codes)




