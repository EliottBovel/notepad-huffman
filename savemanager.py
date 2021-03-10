from math import ceil
import tkinter
import tkinter.filedialog
import os


from binary import Binary
from cbch import cbch
from translate import Translate


class saveManager:
    file = "*.thc"
    rep = os.getcwd()

    def open(self):
        '''
        Permet d'ouvrir un fichier .thc ou .txt pour le lire et le modifier
        :return: (translate) Class translate contenant le texte
        '''
        translate = Translate()

        self.OpenFileDialog()
        if self.file.lower().endswith(".txt"):
            doc = open(self.file, "r", encoding='utf8')
            text = doc.read()
            translate.toBin(text)

            return translate
        binary = Binary()


        if self.file == "":
            return None

        doc = open(self.file, "rb")
        data = self.bytes2binstr(doc.read())
        doc.close()

        dic = ""
        text = ""
        isDic = True
        countLenDic = 0
        for i in range(len(data) // 7 + ceil((len(data) % 7) / 7)):
            value = ""
            for y in range(7):
                b = ""
                if isDic:
                    b = "0"
                if len(data) >= i * 7 + y + 1:
                    b = data[i * 7 + y]
                value += b
            if value == cbch["[SUPERSEP¤]"]:
                isDic = False
            elif isDic:
                countLenDic += 7
            if isDic:
                dic += value
            else:
                if value != cbch["[SUPERSEP¤]"]:
                    text += value

        translate.toText(text[(len(text)%8):], binary.SaveToDict(dic))
        return translate

    def save(self, translate, file=None):
        '''
        Permet d'enregistrer un fichier .thc
        :param translate: (translate) Class translate du texte à enregistrer.
        :param file: (facultatif) (string) lien vers l'emplacement du fichier.
        :return: (boolean) si la sauvegarde s'est bien passée.
        '''
        binary = Binary()

        if file is None:
            self.file = "*.thc"
            self.SaveAsFileDialog()

            if self.file == "":
                return False
        else:
            self.file = file

        if not self.file.lower().endswith(".thc"):
            self.file += ".thc"

        dic = translate.getDict()
        bin = translate.getBin()

        savedic = binary.dictToSave(dic)
        savebin = binary.to255lst(bin)
        save = savedic + savebin

        file = open(self.file, "wb")
        file.write(bytearray(save))
        file.close()

        return True

    def OpenFileDialog(self):
        '''
        Ouvre le la fenêtre de dialogue permettant le choix d'un fichier à ouvrir et stocke le lien dans une variable.
        :return: None
        '''
        win = tkinter.Tk()
        win.withdraw()
        win.iconbitmap("icon.ico")
        filedialog = tkinter.filedialog
        self.file = filedialog.askopenfilename(title="Ouvrir un fichier", initialdir=self.rep, \
                                               initialfile=self.file,
                                               parent=win,
                                               filetypes=[("Fichier Compatibles", "*.thc .txt"), ("Fichier THC", "*.thc"), ("Fichier TXT", "*.txt")])

    def SaveAsFileDialog(self):
        '''
        Ouvre le la fenêtre de dialogue permettant le choix d'un fichier à sauvegarder et stocke le lien dans une variable.
        :return: None
        '''
        win = tkinter.Tk()
        win.withdraw()
        win.iconbitmap("icon.ico")
        filedialog = tkinter.filedialog
        self.file = filedialog.asksaveasfilename(title="Enregistrer sous", initialdir=self.rep, \
                                                 initialfile=self.file,
                                                 parent=win,
                                                 filetypes=[("Fichier THC", "*.thc")])

    def bytes2binstr(self, b, n=None):
        '''
        transforme des bytes en binaire
        :return: (string) binaire
        '''
        s = ''.join(f'{x:08b}' for x in b)
        return s if n is None else s[:n + n // 8 + (0 if n % 8 else -1)]


