# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    word=line.split()
    for i in word:
        if i not in lst:
            lst.append(i)
                
lst.sort()
print(lst)
