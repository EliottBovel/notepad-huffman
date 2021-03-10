from cbch import cbch
from math import ceil


class Binary:
    code = cbch
    code_key_list = list(code.keys())
    code_value_list = list(code.values())

    def to255lst(self, text):
        '''
        Transforme du binaire en list de valeur 0 - 255
        :param text: string (ex: 0110101011101000111010101)
        :return: list[int] (ex: [128, 4, 65])
        '''
        final = []
        for i in range(len(text) // 8 + ceil((len(text) % 8) / 8)):
            value = ""
            for y in range(8):
                data = "0"
                if len(text) >= i * 8 + y + 1:
                    data = text[i * 8 + y]
                value += data
            final.append(int(value, 2))
        return final

    def dictToSave(self, text):
        '''
        Transforme le dictionnaire en list pour la save
        :param text: string (ex: a1;b2;c4)
        :return: list[int] (ex: [128, 4, 65])
        '''
        ntext = ""
        for i in text:
            if i in self.code_key_list:
                ntext += self.code[i]
            else:
                ntext += self.code[""]
        ntext += self.code["[SUPERSEP¤]"]

        while len(ntext) % 8 != 0:
            ntext += "0"

        ntext = list(ntext)
        data = ""
        for i in range(len(ntext) // 7 + ceil((len(ntext) % 7) / 7)):
            valide = True
            old = data
            data = ""
            for y in range(7):
                if len(ntext) >= i*7+y+1:
                    data += ntext[i*7+y]
                else:
                    valide = False
            if valide and old != data and data == self.code[";"]:
                for y in range(7):
                    ntext[i * 7 + y] = self.code["[SEP¤]"][y]

        return self.to255lst(''.join(ntext))

    def SaveToDict(self, binaire):
        '''
        Transforme la partie dictionnaire de la save en texte
        :param save: list[int] (ex: [128, 4, 65])
        :return: string (ex: a1b2c4)
        '''


        text = ""
        for i in range(len(binaire) // 7 + ceil((len(binaire) % 7) / 7)):
            value = ""
            isgood = True
            for y in range(7):
                data = "0"
                if len(binaire) >= i * 7 + y + 1:
                    data = binaire[i * 7 + y]
                else:
                    isgood = False

                value += data
            if isgood:
                text += self.code_key_list[self.code_value_list.index(value)]
        return text