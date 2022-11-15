abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))

line = 'A lot              of spaces'
etc = line.split()
print(etc)

line = 'firts;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))
