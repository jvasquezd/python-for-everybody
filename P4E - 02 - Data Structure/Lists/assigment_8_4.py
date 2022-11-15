fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#print(line.rstrip())

try:
    fh = open(fname)
except FileNotFoundError:
    print("File cannot be opened: ",fname)
    quit()

lst = list()
for line in fh:
    sentences = line.rstrip().split()
    for word in sentences:
        if word not in lst:
            continue
        else:
            lst.append(word)
    #lst.append(p.split())
lst.sort()
print(lst)
