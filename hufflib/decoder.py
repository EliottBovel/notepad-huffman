def est_feuille(node):
    return node.left is None and node.right is None

def decode(text, arbre, cars):
    i = len(text)
    length = len(text)
    final_text = ""
    while i > 0 and cars >0:
        node = arbre
        finish = False
        while not finish and i > 0 and cars >0:
            if est_feuille(node):
                finish = True
                final_text += node.car
                cars-=1
            else:
                if text[length - i] == "0":
                    node = node.left
                elif text[length - i] == "1":
                    node = node.right
                i -= 1
    return final_text