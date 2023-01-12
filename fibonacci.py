def fib(n):
    a = 1
    b = 1
    yield a
    yield b
    for i in range(n-2):
        yield a + b
        a, b = b, a
        a = a + b

fib10 = fib(10)
listFib10 = [item for item in fib10]
print(listFib10)

first_set = set([1, 2, 5])
second_set = set([1, 2, 5, 10])
first_set.difference(second_set) == set()
second_set.difference(first_set) != set()

my_name = 'Edoardo Turri'
first_name, last_name = my_name.split(' ')

full_name_list = my_name.split()
delimiter = ' '
delimiter.join(full_name_list)

dictionary = {'nome':'Edoardo', 'cognome': 'Turri'}
dictionary.keys()
dictionary.values()
dictionary.items()

swapped_dictionary = dict()
for key, value in dictionary.items():
    swapped_dictionary[value] = key

print(swapped_dictionary)

dictionary['ciao']

ral = 1567.95 * 11 + 1660.17 * 2 + 4000
print(ral) 

netto_mensile_orbyta = 1521 + 5.29 * 20