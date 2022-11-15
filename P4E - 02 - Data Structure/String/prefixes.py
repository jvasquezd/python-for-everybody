line = 'Please have a nice day'
print("startswith: ", line.startswith('Please'))

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print('atpos: ', atpos)
sppos = data.find(' ', atpos)
print('sppos: ', sppos)

host = data[atpos+1:sppos]
print('host: ', host)
