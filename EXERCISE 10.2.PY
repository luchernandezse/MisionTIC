#%%
fhand=open('mbox-short.txt')
counts=dict()
F_t=list()
count=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue 
    words=line.split()
    tmpw=words[5]
    tmpw=tmpw.split(':')
    F_t.append((tmpw[0]))
for word in F_t:
    counts[word]=counts.get(word,0)+1
lst=list()
for k,v in counts.items():
    newtup=(k,v) #Crear una lista de tupples
    lst.append(newtup)
lst=sorted(lst)
for v,k in lst:
    print(v,k)
# %%
