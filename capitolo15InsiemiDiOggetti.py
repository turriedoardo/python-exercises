class Carta:
    ListaSemi = ["Fiori", "Quadri", "Cuori", "Picche"]
    ListaRanghi = ["impossibile", "Asso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Regina", "Re"]

    def __init__(self, Seme = 0, Rango = 0) -> None:
        self.Seme = Seme
        self.Rango = Rango

    def __str__(self) -> str:
        return self.ListaRanghi[self.Rango] + " di " + self.ListaSemi[self.Seme]

    def __eq__(self, Altro):
        if self.Seme == Altro.Seme and self.Rango == Altro.Rango: return True
        else: return False

    def __gt__(self, Altro):
        if self.Seme > Altro.Seme: return True
        # gli assi hanno valore maggiore
        elif self.Rango == 1 and Altro.Rango != 1: return True
        elif self.Rango > Altro.Rango: return True
        else: return False

    def __lt__(self, Altro):
        if self.Seme < Altro.Seme: return True
        elif self.Rango != 1 and Altro.Rango == 1: return True
        elif self.Rango < Altro.Rango: return True
        else: return False


class Mazzo:
    def __init__(self) -> None:
        self.Carte = []
        for Seme in range(4):
            for Rango in range(1, 14):
                self.Carte.append(Carta(Seme, Rango))

    def StampaMazzo(self):
        for Carta in self.Carte:
            print(Carta)

    def __str__(self) -> str:
        s = ""
        for i in range(len(self.Carte)):
            s = s + " "*i + str(self.Carte[i]) + "\n"
        return s

    def Mescola(self):
        import random
        NumCarte = len(self.Carte)
        for i in range(NumCarte):
            j = random.randrange(i, NumCarte)
            self.Carte[i], self.Carte[j] = self.Carte[j], self.Carte[i]

            # alternativa senza assegnazione di tuple
            # temp = self.Carte[i]
            # self.Carte[i] = self.Carte[j]
            # self.Carte[j] = temp
    
    def RimuoviCarta(self, Carta):
        if Carta in self.Carte:
            self.Carte.remove(Carta)
            return 1
        else:
            return 0
    
    def PrimaCarta(self):
        return self.Carte.pop()

    def EVuoto(self):
        return(len(self.Carte) == 0)

    def Distribuisci(self, ListaMani, NumCarte = 999):
        NumMani = len(ListaMani)
        for i in range(NumCarte):
            if self.EVuoto(): break
            Carta = self.PrimaCarta()
            Mano = ListaMani[i % NumMani]
            Mano.AggiungeCarta(Carta)



