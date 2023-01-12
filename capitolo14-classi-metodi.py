from fun.clearConsole import clear as cancella
from capitolo12ClassiOggetti import Punto
# from capitolo13ClassiFunzioni import StampaTempo

def Trova(Stringa, Carattere, Inizio = 0, Fine = 0):
    Fine = len(Stringa)
    Indice = Inizio
    ListaIndici = list()
    while Indice < Fine:
        if Stringa[Indice] == Carattere:
            ListaIndici.append(Indice)
        Indice += 1

    if ListaIndici != []:
        print(ListaIndici)
    else:
        return -1


class Tempo:

    def __init__(self, Ore = 0, Minuti = 0, Secondi = 0):
        self.Ore = Ore
        self.Minuti = Minuti
        self.Secondi = Secondi

    def StampaTempo(self):
        print(f'{self.Ore}:{self.Minuti}:{self.Secondi}')

    def Incremento(self, Secondi):
        self.Secondi += Secondi

        while self.Secondi >= 60:
            self.Secondi -= 60
            self.Minuti += 1

        while self.Minuti >= 60:
            self.Minuti -= 60
            self.Ore += 1

    def ConverteInSecondi(self):
        TempoInSecondi = self.Ore * 3600 + self.Minuti * 60 + self.Secondi
        return TempoInSecondi

    def Dopo(self, Tempo2):
        if self.Ore > Tempo2.Ore:
            return True
        elif self.Ore < Tempo2.Ore:
            return False

        if self.Minuti > Tempo2.Minuti:
            return True
        elif self.Minuti < Tempo2.Minuti:
            return False
        
        if self.Secondi > Tempo2.Secondi:
            return True
        return False

OraAttuale = Tempo(9, 30, 56)
OraAttuale = Tempo(Secondi= 50, Ore= 10)
TempoCottura = Tempo(9)

TempoCottura.Ore = 9
TempoCottura.Minuti = 30
TempoCottura.Secondi = 56

OraAttuale.Ore = 10
OraAttuale.Minuti = 14
OraAttuale.Secondi = 30

if OraAttuale.Dopo(TempoCottura):
    print('Il pranzo è pronto')

OraAttuale.Incremento(500)

OraAttuale.StampaTempo()
TempoCottura.StampaTempo()

OraAttuale.ConverteInSecondi()

Trova('Edoardo', 'o')

P1 = Punto(10, 5)
P2 = Punto(1, 4)
P3 = P1 * P2
print(P3)