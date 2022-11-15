fname = input("Enter the file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened: ",fname)
    quit()

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())