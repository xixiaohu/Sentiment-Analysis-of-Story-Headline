import sys

#get data from standard input
data = sys.stdin.readlines()

#get positive words from txt file
pwords = open('positive-words.txt',  'r')
positive = []
for line in pwords.readlines():
    line = line.strip()
    if not line.startswith(';'):
        positive.append(line[1:])

#get negative words from txt file
nwords = open('negative-words.txt', 'r', encoding='ISO-8859-1' )

negative = []
for line in nwords.readlines():
    line = line.strip()
    if not line.startswith(';'):
        negative.append(line[1:])

#mapping positive and negative words
worddict = {}
for line in data:
    line = line.strip()
    for words in line.split():
        if words in positive:
            if words in worddict.keys():
                worddict[words] += 1 
            else: 
                worddict[words] = 1 
        elif words in negative:
            if words in worddict.keys():
                worddict[words] += -1 
            else: 
                worddict[words] = -1

# print out results               
for key in worddict.keys():
    print(key,",",worddict[key])
