filename = "dataset/mbox-short.txt"
name = input("Enter file:")
handle=open(name)
counts=dict()
lst=list()
for line in handle:
    words=line.split()
    if 'From:' in line:
        counts[words[1]]=counts.get(words[1],0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
