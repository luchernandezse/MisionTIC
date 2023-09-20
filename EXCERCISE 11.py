#%%
import re
hand=open('regex_sum_941224.txt')
numlist=list()
total=0
for line in hand:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    stuff = [int(i) for i in stuff] 
    for ele in range(0, len(stuff)):
        total = total + stuff[ele]
print(total)
# %%
