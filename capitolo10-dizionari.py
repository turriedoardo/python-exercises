import chapter1

# creo dizionario vuoto
Eng2Ita = {}
Eng2Ita['one'] = 'uno'
Eng2Ita['two'] = 'due'

magazzino = {'mele':430, 'pere': 217, 'banane': 312, 'arance':525}
nuovoMagazzino = magazzino
del nuovoMagazzino

# per eliminare le pere dal magazzino
del magazzino['pere']
print(magazzino)

# reimposto le pere uguali a zero
magazzino['pere'] = 0

#### METODI DEI DIZIONARI
# stampo le chiavi del dizionario
magazzino.keys()

# stampo i valori
magazzino.values()

# coppie chiavi-valore come lista di tuple
magazzino.items()

# controllare se la chiave appartiene al dizionario
print('mele' in magazzino)

# creo dizionario opposti
opposti = dict(alto = 'basso', giusto = 'sbagliato', vero = 'falso')
print(opposti)

# alias non è un nuovo dizionario, è un altro modo per riferirsi a quello appena definito
alias = opposti

# copia è un altro dizionazio, identico a opposti
copia = opposti.copy()

# posso usare delle tuple come chiavi del dizionario
matrice = {(0, 3): 1, (2,1): 2, (4,3): 3}
matrice[(0, 3)]

# ritorna 0 quando non trova il primo argomento (la tupla) nel dizionario
matrice.get((1, 3), 0)

# 10.5 Suggerimenti