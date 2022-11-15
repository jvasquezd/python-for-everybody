
han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    #if line == '':
    #    continue
    #if len(wds) < 1:
    #    continue
    #guardian in a compund statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])