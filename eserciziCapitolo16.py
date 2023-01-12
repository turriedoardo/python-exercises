from capitolo15InsiemiDiOggetti import Mazzo, Carta
from capitolo16Ereditarieta import *

Mazzo1 = Mazzo()
Mazzo1.Mescola()
Mano1 = Mano('pippo')
Mazzo1.Distribuisci([Mano1], 5)
print(Mano1)

MyOldMaid = GiocoOldMaid()
MyOldMaid.Partita(Nomi = ['Edoardo'])
print(MyOldMaid.Mani[0].Nome)
