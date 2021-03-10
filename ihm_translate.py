from tkinter import *
from tkinter import tix

import pyperclip

from translate import Translate


class IHMTranslate:
    __dim = (1200, 700)
    __Icon = "icon.ico"

    def __init__(self, **args):
        self.__root = Tk()

        self.__TextArea = Text(self.__root, undo=True)
        self.__TextTranslatedArea = Text(self.__root)
        self.__ListDict = Listbox(self.__root, width=30)

        self.__TextArea.bind("<KeyRelease>", self.__update)
        self.__TextTranslatedArea.bind("<KeyRelease>", self.__blockUpdate)
        self.__TextArea.bind("<Double-ButtonRelease>", self.__copytext)
        self.__TextTranslatedArea.bind("<Double-ButtonRelease>", self.__copybin)

        self.__root.resizable(width=False, height=False)

        self.__TextTranslatedArea.insert(1.0, "le code Huffman apparaitera ici !")
        self.__ListDict.insert(0, "Dictionnaire:")

        # On défini toutes les caractéristiques de la fenêtre
        self.__root.title("Traducteur Huffman")

        try:
            self.__Icon = args['icon']
        except KeyError:
            pass

        try:
            self.__root.wm_iconbitmap(self.__Icon)
        except:
            pass

        try:
            self.__thisWidth = args['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = args['height']
        except KeyError:
            pass

        # On gère la taille et l'alignement
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__dim[0] / 2)
        top = (screenHeight / 2) - (self.__dim[1] / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__dim[0],
                                              self.__dim[1],
                                              left, top))

        self.__root.grid_rowconfigure(0, weight=2)
        self.__root.grid_columnconfigure(0, weight=4)

        self.__TextArea.grid(column=0, columnspan=3, row=0, sticky=N + W + E)
        self.__TextTranslatedArea.grid(column=0, columnspan=3, row=1, sticky=S + W + E)
        self.__ListDict.grid(column=3, row=0, rowspan=2, sticky=N + E + S + W)

        #fonctionne pas
        self.__TextArea.mark_set("insert", "%d.%d" % (1,1))

        self.__root.protocol("WM_DELETE_WINDOW", self.__quit)


    def __quit(self):
        self.__root.destroy()

    def __update(self, event):
        tr = Translate()
        text = self.__TextArea.get(1.0, END)[:-1]
        if len(text) > 0:
            bin = tr.toBin(text)
            doubles = tr.getDoubles()

            self.__TextTranslatedArea.delete(1.0, END)
            self.__TextTranslatedArea.insert(1.0, bin)
            self.__ListDict.delete(1, END)

            doubles = sorted(doubles, key=lambda x: x[1])
            doubles.reverse()
            for d in doubles:
                if len(d) == 2:
                    letter = d[0]
                    count = d[1]
                    if letter == " ":
                        letter = "[SPACE]"
                    elif letter == "µ":
                        letter = "[NewLine]"
                        count -= 0
                    if count > 0:
                        self.__ListDict.insert(self.__ListDict.size(), letter + ": " + str(count))

        else:
            self.__TextTranslatedArea.delete(1.0, END)
            self.__TextTranslatedArea.insert(1.0, "le code Huffman apparaitera ici !")
            self.__ListDict.delete(1, END)

    def __blockUpdate(self, event):
        self.__update(None)

    def __copytext(self, event):
        text = self.__TextArea.get(1.0, END)
        if text != "":
            pyperclip.copy(text)

    def __copybin(self, event):
        text = self.__TextTranslatedArea.get(1.0, END)
        if text != "":
            pyperclip.copy(text)

    def run(self):
        self.__root.mainloop()
