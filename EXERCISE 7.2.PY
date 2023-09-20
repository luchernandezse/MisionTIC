fname2=input('Enter File Name:  ')
try:
    fhand=open(fname2)
    print(fhand)
except:
    print('File Cannot be oppened: ',fname2)
count=0
s_val=0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    ipos=line.find(':')
    piece=line[ipos+1:]
    value=float(piece)
    s_val=s_val+value
prom=s_val/count
print('Average spam confidence:',prom)

