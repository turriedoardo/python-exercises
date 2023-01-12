import pandas as pd
import os
import sys
import numpy
import array

def clear():
    os.system('cls')

# stampo versione corrente di python
print(sys.version)

a = 1+1
print(a)

fatturato = pd.read_excel('query-testata-dettaglio.xlsx')

os.getcwd()

# informazioni sul dataset
fatturato.head()
fatturato.columns
fatturato.info()
fatturato.describe()

conteggio_nulli_fatturato = fatturato.annomese.isnull().sum()
print(conteggio_nulli_fatturato)

lista_annomesi = fatturato.annomese.to_list()
print(lista_annomesi[-1])
print(lista_annomesi[1])

array_vuoto = numpy.empty(shape=(0, 0))
print(array_vuoto)

a = [1,2,3]
# terz ultimo elemento della lista a
print(a[-3])

subjects = ('python', 'interview', 'questions')
print(type(subjects))

for contatore, parola in enumerate(subjects):
    print(contatore, parola)

# somma dei numeri da 1 a 100
somma_primi_cento = sum(range(1, 101))
print(somma_primi_cento)

# stabilitre l'output
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0

# ad ogni iterazione, ls assume il valore di una delle liste tra parentesi
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)

def printa():
    a = 12
    print(a)

printa()

