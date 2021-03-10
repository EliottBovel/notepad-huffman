import os
from tkinter import *
from tkinter.messagebox import *

import ihm_translate
from savemanager import saveManager
from translate import Translate

class IHM:
    __root = Tk()

    __dim = (1200, 700)
    __TextArea = Text(__root, undo=True)
    __MenuBar = Menu(__root)
    __FileMenu = Menu(__MenuBar, tearoff=0)
    __EditMenu = Menu(__MenuBar, tearoff=0)
    __HelpMenu = Menu(__MenuBar, tearoff=0)
    __Icon = "icon.ico"

    __ScrollBar = Scrollbar(__TextArea)
    __file = None

    __Translate = Translate()

    def __init__(self, **args):

        # On défini toutes les caractéristiques de la fenêtre
        self.__root.title("Aucun Nom - Bloc-Note Huffman")

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

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # On ajoute les éléments à la fenêtre
        self.__TextArea.grid(sticky=N + E + S + W)

        self.__FileMenu.add_command(label="Nouveau (Ctrl+N)", command=self.__newFile)
        self.__FileMenu.add_command(label="Ouvrir (Ctrl+O)", command=self.__openFile)
        self.__FileMenu.add_command(label="Enregistrer (Ctrl+S)", command=self.__saveFile)
        self.__FileMenu.add_command(label="Enregistrer sous (Ctrl+Maj+S)", command=self.__saveAsFile)
        self.__FileMenu.add_command(label="Imprimer (Ctrl+P)", command=self.__print)
        self.__FileMenu.add_separator()
        self.__FileMenu.add_command(label="Traduire (Ctrl+T)", command=self.__translator)
        self.__FileMenu.add_separator()
        self.__FileMenu.add_command(label="Quitter", command=self.__quit)
        self.__MenuBar.add_cascade(label="Fichier", menu=self.__FileMenu)
        self.__EditMenu.add_command(label="Couper", command=self.__cut)
        self.__EditMenu.add_command(label="Copier", command=self.__copy)
        self.__EditMenu.add_command(label="Coller", command=self.__paste)
        self.__MenuBar.add_cascade(label="Modifier", menu=self.__EditMenu)
        self.__HelpMenu.add_command(label="Version", command=self.__showVersion)
        self.__HelpMenu.add_command(label="A propos", command=self.__showAbout)
        self.__MenuBar.add_cascade(label="Aide", menu=self.__HelpMenu)

        self.__root.config(menu=self.__MenuBar)

        self.__ScrollBar.pack(side=RIGHT, fill=Y)

        self.__ScrollBar.config(command=self.__TextArea.yview)
        self.__TextArea.config(yscrollcommand=self.__ScrollBar.set)

        # On ajoute les raccourcis claviers
        self.__root.bind("<Control-Key-n>", self.__racNew)
        self.__root.bind("<Control-Key-N>", self.__racNew)
        self.__root.bind("<Control-Key-o>", self.__racOpen)
        self.__root.bind("<Control-Key-O>", self.__racOpen)
        self.__root.bind("<Control-Key-s>", self.__racSave)
        self.__root.bind("<Control-Key-S>", self.__racSave)
        self.__root.bind("<Control-Key-s><Key-Caps_Lock>", self.__racSaveAs)
        self.__root.bind("<Control-Key-S><Key-Caps_Lock>", self.__racSaveAs)
        self.__root.bind("<Control-Key-p>", self.__racPrint)
        self.__root.bind("<Control-Key-P>", self.__racPrint)
        self.__root.bind("<Control-Key-t>", self.__racTranslate)
        self.__root.bind("<Control-Key-T>", self.__racTranslate)

        # event: user close window
        self.__root.protocol("WM_DELETE_WINDOW", self.__quit)

    def __quit(self):
        self.__root.destroy()
        exit()

    def __showAbout(self):
            showinfo("Bloc-Note Huffman", "Le Bloc-Note Huffman est un logiciel open-source.\n\
    Version 0.2 - En cours de développement\n\n\
    Développé dans le cadre d'un projet scolaire visant au développement d'une IHM en python\n\n\
    Par Eliott Bovel et Bastien Gérard.\n\
    Lycée Notre-Dame des Aydes, Terminal 1, Spé NSI - 2020/2021")

    def __showVersion(self):
        showinfo("Bloc-Note Huffman", "Version Béta 0.1 - En cours de développement")

    def __openFile(self):

        save = saveManager()
        tr = save.open()

        self.__file = save.file

        if self.__file == "":

            self.__file = None
        else:
            self.__Translate = tr

            self.__root.title(os.path.basename(self.__file) + " - Bloc-Note Huffman")
            self.__TextArea.delete(1.0, END)

            file = tr.getText()

            self.__TextArea.insert(1.0, file)


    def __newFile(self):
        self.__root.title("Aucun Nom - Bloc-Note Huffman")
        self.__file = None
        self.__TextArea.delete(1.0, END)
        self.__Translate = Translate()

    def __saveFile(self):
        if self.__file is None:
            self.__saveAsFile()
            return
        else:
            save = saveManager()
            self.__Translate.toBin(self.__TextArea.get(1.0, END))
            save.save(self.__Translate, self.__file)


    def __saveAsFile(self):
        save = saveManager()
        self.__Translate.toBin(self.__TextArea.get(1.0, END))
        isSave = save.save(self.__Translate)

        if isSave:
            self.__file = save.file
            self.__root.title(os.path.basename(self.__file) + " - Bloc-Note Huffman")



    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __print(self):
        #text = self.__TextArea.get(1.0, END)

        #filename = tempfile.mktemp(".txt")
        #open(filename, "w").write(text)
        #pywin32.win32api.ShellExecute(0,  "print",  filename, None, ".", 0)
        showinfo('Bloc-Note Huffman', "La fonction 'imprimer' n'est pas encore disponible.")

    def __translator(self):
        translate = ihm_translate.IHMTranslate()
        translate.run()

    def run(self):
        self.__root.mainloop()

    def __racNew(self, event):
        self.__newFile()

    def __racOpen(self, event):
        self.__openFile()

    def __racSave(self, event):
        self.__saveFile()

    def __racSaveAs(self, event):
        self.__saveAsFile()

    def __racPrint(self, event):
        self.__print()

    def __racTranslate(self, event):
        self.__translator()

