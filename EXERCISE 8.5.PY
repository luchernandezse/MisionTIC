fhand=open('mbox-short.txt')
count=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue 
    count=count+1
    words2=line.split()
    email=words2[1]
    print(email)
print("There were", count, "lines in the file with From as the first word")