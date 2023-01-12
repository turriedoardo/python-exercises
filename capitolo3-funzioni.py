# funzioni matematiche
import math
from fun.clearConsole import clear as cancella

# quando converte in intero viene troncata la parte decimale, non arrotondata
print(int(3.99))

# questa conversione restituisce un errore
int('3.98032')


# log in base 10 di 17
decibel = math.log10(17)
print(decibel)

angoloInGradi = 45
angoloInRad = angoloInGradi/360 * 2 * math.pi
senoAngolo = math.sin(angoloInRad)
print(senoAngolo)

# esercizio
def stampa2volte(valore):
    print(valore, valore)

def unaRigaVuota():
    print()

stampa2volte('"Pippo"*4')

messaggio = 'come va?'
stampa2volte(messaggio)

unaRigaVuota() + 7
