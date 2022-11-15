counts = dict()
print("Enter a line of next: ")
line = input('')
words = line.split()

print("Words:", words)

print("Counting")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts", counts)

"""The general pattern to count the words 
in a line of text is to split the line into words, 
then loop through the words and use a dictionary
to track the count of each word independently"""