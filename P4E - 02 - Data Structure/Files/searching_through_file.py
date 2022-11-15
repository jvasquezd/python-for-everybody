fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        
# este programa imprime linea a linea todo el contenido
# de un archivo