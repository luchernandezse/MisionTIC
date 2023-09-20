fhand=open('romeo.txt')
F_t=list()
count=0
for line in fhand:
    line=line.rstrip()
    wd=(line.split())
    a=range(len(wd))
    for i in a:
        count=count+1
        b=wd[i]
        if b in F_t:
            continue
        else:
            F_t.append((b))

F_t.sort()
print(F_t)


