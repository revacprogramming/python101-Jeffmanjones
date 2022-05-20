# Dictionaries

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
handle=open(name)
counts=dict()
lst=list()
for line in handle:
    words=line.split()
    if
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
        
print(bigword,bigcount)