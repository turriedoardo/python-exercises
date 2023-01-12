ages = dict(Giovanni = 43, Matt = 30, Katie = 29, Jack = 43)
max(ages, key = ages.get) # ages.get significa che il criterio per selezionare il massimo è il valore corrispondente alla chiave
ages.get('Matt')

[age for age in ages.values()]
values_list = list(ages.values())
sum(values_list)

print('ciao')
exit()
print('questa riga non dovrebbe essere stampata')