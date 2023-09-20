#%%
fhand=open('mbox-short.txt')
counts=dict()
F_t=list()
count=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue 
    words=line.split()

    F_t.append((words[1]))

for word in F_t:
    counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for word1,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word1
        bigcount=count
print(bigword,bigcount)
# %%
