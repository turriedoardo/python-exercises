import pickle

f = open('test.dat', 'w')
print(f)
f.write('Adesso')
f.write('chiudi il file')

f.close()

f = open('test.dat', 'r')
Testo = f.read(5)
print(Testo)

def CopiaFile(Originale, Copia):
    f1 = open(Originale, 'r')
    f2 = open(Copia, 'w')
    while True:
        Testo = f2.read(50)
        if Testo == '':
            break
        else:
            f1.write(Testo)
    f1.close()
    f2.close()
    return

f = open('test.dat', 'w')
f.write('linea uno\nlinea due\nlinea tre')
f.close()

# utilizzando un context manager il file viene chiuso automaticamente
with open('test.dat', 'r') as f:
    print(f.readline())
    print(f.readlines())
    print(f.readline())
    print(f.readlines())

# 11.2
x = 52.3
f = open('test.dat','w')
f.write('\n' + str(x))

'%d' % x
print('%-10s ciao' % 'parola')

# directory
laMiaLista = ['ciao', 4, True]
str(laMiaLista)

with open('test.pck', 'wb') as f:
    pickle.dump(12.3, f)
    pickle.dump(4.567, f)
    pickle.dump([1,2,3], f)

f = open('test.pck', 'rb')
x = pickle.load(f)
print(x)

x2 = pickle.load(f)
print(x2)

laMiaNuovaLista = pickle.load(f)
print(laMiaNuovaLista[2])
type(laMiaNuovaLista)

NomeFile = input('Inserisci il nome del file: ')

try:
    f = open(NomeFile, 'r')
except:
    print(f'Il file {NomeFile} non esiste.')


def InputNumero():
    x = input('Dimmi un numero: ')
    x = int(x)
    if x > 16:
        raise Exception('mi aspetto numeri minori di 17')
    return x

InputNumero()

def GestioneInputNumero():
    try:
        numero = InputNumero()
        return numero
    except Exception as e:
        print(f'La funzione ha prodotto il seguente errore: {e}')

# finito