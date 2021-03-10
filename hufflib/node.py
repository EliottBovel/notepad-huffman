#--------------------------------------------
# Codage de Huffman
# Construction de l'arbre du texte
# CWZ Février 2021
#-------------------------------------------

class Node :
    def __init__(self, symbol, freq, left=None, right=None) :
        self.car=symbol
        self.nb=freq
        self.left = left
        self.right = right

def affiche(arb):
    '''affiche sur la console la description de arb'''
    if arb.left == None and arb.right == None:
        print( arb.car,' - ',arb.nb )
    
    elif arb.left == None :
        
        affiche (arb.right)
        print( ' noeud droit ',arb.car,' - ',arb.nb )
    elif arb.right == None :
        print( ' noeud gauche ',arb.car,' - ',arb.nb )
        affiche (arb.right)
       
    else :
        print( 'noeud centre ',arb.car,' - ',arb.nb )
        affiche (arb.left)
        affiche (arb.right)
        
        
        
def echange (L,i,j):
    ''' echange les indices i et j de la liste L'''
    L[i],L[j] = L[j],L[i]

def minimum (L,i):
    ''' cherche l'élément de la liste L dont l'attrinut nb est le
    plus petit à partir de l'indice i'''
    i_noeud_min = i
    nb_noeud_min = L[i].nb
    for j in range (i+1,len(L)):
        if L[j].nb < nb_noeud_min :
            i_noeud_min = j
            nb_noeud_min = L[j].nb
    return i_noeud_min
    

def trier (ma_liste):
    '''tri de liste de noeuds sur l'attribut nb'''
    for i in range(len(ma_liste)) :
        ind_noeud_min = minimum (ma_liste,i)
        echange (ma_liste,i,ind_noeud_min)
        

def create (car_occur):
    '''récupérere la liste de tuples pour créer l'arbre de compression'''
    liste_car_occ = []
    #créer une liste de Node, une par caractère
    for t in car_occur :
        liste_car_occ.append (Node(t[0],t[1]))

    #tant que cette liste a plus d'un élément, on le complète
    #On suppose que il y a au moins 2 éléments ?
    while len(liste_car_occ) > 1:
        liste_car_occ[0] = Node(liste_car_occ[0].nb+liste_car_occ[1].nb,
                                liste_car_occ[0].nb+liste_car_occ[1].nb,
                                liste_car_occ[0],
                                liste_car_occ[1])
        liste_car_occ.pop(1)
        trier(liste_car_occ)
    #quand cette liste a un seul élément, c'est l'arbre attendu
    return liste_car_occ[0]

