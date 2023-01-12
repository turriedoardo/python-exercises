from capitolo15InsiemiDiOggetti import Mazzo, Carta

# creo la classe Mano, sottoclasse di Mazzo
class Mano(Mazzo):
    def __init__(self, Nome = ""):
        super().__init__()
        self.Carte = []
        self.Nome = Nome

    def AggiungeCarta(self, Carta):
        self.Carte.append(Carta)

    def __str__(self) -> str:
        s = f'La mano di {self.Nome}'
        if self.EVuoto():
            s = f'{s} è vuota\n'
        else:
            s = f'{s} contiene queste carte:\n{Mazzo.__str__(self)}'
        return s

class GiocoDiCarte:
    def __init__(self) -> None:
        self.Mazzo = Mazzo()
        self.Mazzo.Mescola()

class ManoOldMaid(Mano):

    def RimuoveCoppie(self):
        Conteggio = 0
        CarteOriginali = self.Carte[:]
        for CartaOrig in CarteOriginali:
            CartaDaCercare = Carta(3 - CartaOrig.Seme, CartaOrig.Rango)
            if CartaDaCercare in self.Carte:
                self.Carte.remove(CartaOrig)
                self.Carte.remove(CartaDaCercare)
                print(f'Mano di {self.Nome}: {CartaOrig} elimina {CartaDaCercare}')
                Conteggio = Conteggio + 1
        return Conteggio

class GiocoOldMaid(GiocoDiCarte):
    
    def Partita(self, Nomi):
        # rimuovo la regina di fiori
        self.Mazzo.RimuoviCarta(Carta(0, 12))

        # creo una mano per ogni giocatore
        self.Mani = []
        for Nome in Nomi:
            self.Mani.append(ManoOldMaid(Nome))

        # distribuzione delle carte
        self.Mazzo.Distribuisci(self.Mani)
        print('--------- Le carte sono state distribuite')
        self.StampaMani()

        # tolgo le coppie nella stessa mano
        NumCoppie = self.RimuoveTutteLeCoppie()
        print('--------- Coppie scartate, inizia la partita')
        self.StampaMani()

        # il gioco prosegue fino a che non sono state fatte 25 copie
        Turno = 0
        NumMani = len(self.Mani)
        while NumCoppie < 25:
            NumCoppie = NumCoppie + self.GiocaUnTurno(Turno)
            Turno = (Turno + 1) % NumMani

        print('--------- La partita è finita')
        self.StampaMani()

    def RimuoveTutteLeCoppie(self):
        Conteggio = 0
        for Mano in self.Mani:
            Conteggio = Conteggio + Mano.RimuoveCoppie()
        return Conteggio

    def StampaMani(self):
        for Mano in self.Mani:
            print(Mano)

    def GiocaUnTurno(self, Giocatore):
        if self.Mani[Giocatore].EVuoto():
            return 0
        Vicino = self.TrovaVicino(Giocatore)
        CartaScelta = self.Mani[Vicino].PrimaCarta()
        self.Mani[Giocatore].AggiungeCarta(CartaScelta)
        print(f'Mano di {self.Mani[Giocatore].Nome}: scelta {CartaScelta}')
        Conteggio = self.Mani[Giocatore].RimuoviCoppie()
        self.Mani[Giocatore].Mescola()
        return Conteggio

    def TrovaVicino(self, Giocatore):
        NumMani = len(self.mani)
        for Prossimo in range(1, NumMani):
            Vicino = (Giocatore + Prossimo) % NumMani
            if not self.Mani[Vicino].EVuoto():
                return Vicino
