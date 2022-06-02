fname = "python.txt"
num_words = 0
f= open(fname, 'r')
words = f.read().split()
for a in words:
  if (a.tolower() == “to” or a.tolower() == “the” ):
    num_words = num_words + 1
print("Number of words:", num_words)
f.close()