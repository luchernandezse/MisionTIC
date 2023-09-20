#%%
import re
x='My 2 favourite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)
y=re.findall('[AEIOUM]+',x)
print(y)
#GREEDY MATCH: Se busca cumplir la condicion lo mas extensa posible
x='From: Using the: character'
y=re.findall('^F.+:',x)
print(y)
#se incluye una re "?" para quitar el efecto greedy
y=re.findall('^F.+?:',x)
print(y)
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('\S+@\S+',x)
print(y)
#Se puede extraer un pedazo de una condicion
y=re.findall('^From (\S+@\S+)',x)#asuguramos que la ilnea arranque con la palabra "From "
print(y)
# Extract the host nime using strings
atpos=x.find('@')
sppos=x.find(' ',atpos)
host=x[atpos+1:sppos]
print(host)
# Double split pattern
word=x.split()
email=word[1]
pieces=email.split('@')
print(pieces[1])
# Regular Expressions
y=re.findall('@([^ ]*)',x)
print(y)
# extraer con caracteristicas especificas
hand=open('mbox-short.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) !=1: continue
    num=float(stuff[0])
    numlist.append(num)
print('Maximun:', max(numlist))
# si se quiere un caracter que forma una re se adiciona "\"
x='We just received $10.00 for cookies.'
y=re.findall('\$[0-9.]+',x)
print(y)
# %%
