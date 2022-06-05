# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()
    
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    a=float(line[20:])
    total=total+a
    
avg=total/count
