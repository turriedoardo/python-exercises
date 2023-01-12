from fun.clearConsole import clear as cancella
import math
import copy

class Punto:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__ (self, AltroPunto):
        return Punto(self.x + AltroPunto.x, self.y + AltroPunto.y)

    def __sub__(self, AltroPunto):
        return Punto(self.x - AltroPunto.x, self.y - AltroPunto.y)

    def __mul__(self, AltroPunto):
        return self.x * AltroPunto.x + self.y * AltroPunto.y
    
    def __rmul__(self, Scalare):
        return Punto(self.x * Scalare, self.y * Scalare)

    def reverse(self):
        self.x, self.y = self.y, self.x


P1 = Punto(3, 4)
P1.x = 3
P1.y = 4
str(P1)
print(P1) # -> si modifica anche print perchè al suo interno viene chiamata str

P2 = Punto()
P2.x = 5
P2.y = 2

P3 = P1 + P2
P4 = P1 - P2
P5 = P1 * P2
print(P5)

hex(id(P2))

def StampaPunto(Punto):
    print(f'{str(Punto.x)}, {str(Punto.y)}')

StampaPunto(P1)

def DistanzaTraDuePunti(Punto1, Punto2):
    dx = Punto1.x - Punto2.x
    dy = Punto1.y - Punto2.y
    DistQuadrata = dx**2 + dy**2
    Risultato = math.sqrt(DistQuadrata)
    return Risultato

def StessoPunto(Punto1, Punto2):
    return (Punto1.x == Punto2.x) and (Punto1.y == Punto2.y)

StessoPunto(P1, P2)

# classe Rettangolo
class Rettangolo:
    pass

Rett = Rettangolo()
Rett.Larghezza = float(100)
Rett.Altezza = float(200)

# posso inserire oggetto punto all'intero di un oggetto rettangolo
Rett.AltoSinistra = Punto()
Rett.AltoSinistra.x = 0
Rett.AltoSinistra.y = 0

def TrovaCentro(Rettangolo):
    P = Punto()
    P.x = Rettangolo.AltoSinistra.x + Rettangolo.Larghezza/float(2)
    P.y = Rettangolo.AltoSinistra.y - Rettangolo.Altezza/float(2)
    return P

Centro = TrovaCentro(Rett)
StampaPunto(Centro)

def AumentaRettangolo(Rettangolo, AumentoLargh, AumentoAlt):
    Rettangolo.Larghezza += AumentoLargh
    Rettangolo.Altezza += AumentoAlt

R1 = Rettangolo()
R1.Larghezza = float(100)
R1.Altezza = float(200)
R1.AltoSinistra = Punto()
R1.AltoSinistra.x = 0.0
R1.AltoSinistra.y = 0.0
AumentaRettangolo(R1, 50, 100)

def MuoviRettangolo(Rettangolo, dx, dy):
    NuovoRett = copy.deepcopy(Rettangolo)
    NuovoRett.AltoSinistra.x += dx
    NuovoRett.AltoSinistra.y += dy
    return NuovoRett

StampaPunto(P1)

