import copy
class Tempo:
    pass

Time = Tempo()
Time.Ore = 11
Time.Minuti = 59
Time.Secondi = 30

def StampaTempo(Tempo):
    print(f'{Tempo.Ore}:{Tempo.Minuti}:{Tempo.Secondi}')

StampaTempo(Time)
def Dopo(Tempo1, Tempo2):
    if Tempo1.Ore > Tempo2.Ore:
        return True
    elif Tempo1.Ore == Tempo2.Ore:
        if Tempo1.Minuti > Tempo2.Minuti:
            return True
        elif Tempo1.Minuti == Tempo2.Minuti:
            if Tempo1.Secondi > Tempo2.Secondi:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


T2 = Tempo()
T2.Ore = 10
T2.Minuti = 50
T2.Secondi = 30

Dopo(Time, T2)

# modificatore
def incremento(Tempo, Secondi):
    Tempo.Secondi += Secondi
    Tempo.Minuti = Tempo.Secondi//60 + Tempo.Minuti
    Tempo.Secondi = Tempo.Secondi % 60
    Tempo.Ore = Tempo.Minuti//60 + Tempo.Ore
    Tempo.Minuti = Tempo.Minuti % 60

# funzione pura
def incremento(Tempo, Secondi):
    TempoAumentato = copy.copy(Tempo)
    TempoAumentato.Secondi += Secondi
    TempoAumentato.Minuti = TempoAumentato.Secondi//60 + TempoAumentato.Minuti
    TempoAumentato.Secondi = TempoAumentato.Secondi % 60
    TempoAumentato.Ore = TempoAumentato.Minuti//60 + TempoAumentato.Ore
    TempoAumentato.Minuti = TempoAumentato.Minuti % 60
    return TempoAumentato

TempoIncrementato = incremento(T2, 3600)
StampaTempo(TempoIncrementato)

StampaTempo(T2)

# utilizzo delle funzioni ausiliarie per ottenere lo stesso risultato

def ConverteInSecondi(Tempo):
    Secondi = Tempo.Ore * 3600 + Tempo.Minuti * 60 + Tempo.Secondi
    return Secondi

def ConverteInTempo(Secondi):
    Orario = Tempo()
    Orario.Ore = Secondi//3600
    Secondi = Secondi%3600
    Orario.Minuti = Secondi//60
    Orario.Secondi = Secondi%60
    return Orario

def incremento(Tempo, Secondi):
    TempoInSecondi = ConverteInSecondi(Tempo)
    TempoIncrementato = TempoInSecondi + Secondi
    return ConverteInTempo(TempoIncrementato)

TempoAumentato = incremento(T2, 3000)
StampaTempo(TempoAumentato)
    
