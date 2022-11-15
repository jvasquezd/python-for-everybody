# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
s = 0.0
try:
    fh = open(fname)
except FileNotFoundError:
    print("File cannot be opened: ",fname)
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        apos = line.find(":")
        num = line[apos+1:]
        afnum = float(num.strip())
        s = s + afnum
        count = count + 1 
    # print(afnum)
average = s / count
print("Average spam confidence:", average)
