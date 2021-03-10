from tkinter.messagebox import *

from hufflib import utils, node, codage, traduction, decoder


class Translate:
    doubles = None
    dict = None
    bin = None
    text = None

    def defineDict(self, dic):
        '''
        Redéfini le dictionnaire Huffman pour le décodage.
        :param dic: (string) Dictionnaire Huffman
        '''
        lst = []
        for element in dic.split("[SEP¤]"):

            el = [element[0], element[1:]]
            if (len(el) >= 2):
                assert isinstance(el[0], str) and isinstance(el[1], str), showerror("Bloc-Note Huffman", "Votre dictionnaire n'est pas valide.")
                assert self.representsInt(el[1]), showerror("Bloc-Note Huffman", "Votre dictionnaire n'est pas valide.")

                lst.append((el[0], int(el[1])))
        self.doubles = lst
        self.dict = node.create(self.doubles)

    def toText(self, bin, dict=None):
        '''
        Décode un code huffman et le renvoie
        :param bin: Code Huffman
        :param dict: (facultatif) (string) Dictionnaire Huffman
        :return: (string) texte décodé
        '''
        if dict is not None:
            self.defineDict(dict)
        self.bin = bin
        dec = decoder.decode(bin, self.dict, self.countCars())
        dec = dec.replace("µ", "\n")
        self.text = dec
        return dec

    def toBin(self, text):
        '''
        Code un texte en code huffman
        :param text: (string) Texte à coder
        :return: (string binaire) code huffman
        '''
        text = text.replace("µ", "")
        text = text.replace("\n", "µ")
        self.doubles = utils.getDoubles(text)
        self.dict = node.create(self.doubles)
        self.bin = traduction.encodage(text, self.dict)
        self.text = text
        return self.bin

    def getDict(self):
        '''
        :return: (string) Dictionnaire huffman
        '''
        string = ""
        for element in self.doubles:
            string += element[0] + str(element[1]) + ";"

        return string[:-1]

    def getBin(self):
        '''
        :return: (string binaire) code huffman
        '''
        return self.bin

    def getDoubles(self):
        '''
        :return: (list[doubles]) dictionnaire huffman sous form de liste
        '''
        return self.doubles

    def getText(self):
        '''
        :return: (string) dernier texte codé
        '''
        return self.text

    def countCars(self):
        '''
        Compte le nombre de caractère total dans le dictionnaire
        :return: (int) nombre de caractère
        '''
        cars = 0
        for i in self.doubles:
            cars += i[1]
        return cars

    def representsInt(self, text):
        '''
        Vérifie si un string peut-etre un integer
        :param text: (string)
        :return: (boolean)
        '''
        try:
            int(text)
            return True
        except ValueError:
            return False
