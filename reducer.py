import sys

#list of scores
totalscore = []

#read from standard input
for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    totalscore.append(int(words[1]))
    
print ("The final index score of content is: ", sum(totalscore))
