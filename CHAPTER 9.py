#%%
purse = dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print(purse)
print(purse['candy'])
purse['candy']=purse['candy']+2
print(purse)
# %%
#Empty Dictioanries
jjj={'chuck':1,'fref':42,'jan':100}
print (jjj)
ooo={}
print(ooo)
# %%
ccc=dict()
ccc={'csev':1,'cwen':1}
print(ccc)
ccc['csev']=ccc['csev']+1
print(ccc['csev'])
#Busca si hay o no un key en la variable de diccionario
'dwen' in ccc
# %%
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names :
    if name not in counts:
        counts[name]=1
    else :
        counts[name]=counts[name]+1
print(counts)
# %%
# la funcion .get permite ahorrar lineas de codigo
#Funcion como el condicional, si encuentra la variable name toama su vaor anterior +1
#si no, entonces asigna un valor por default de cero 0 [name,0] y crea la variable
#le suma uno
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names :
    counts[name]=counts.get(name,0)+1
print(counts)
# %%
counts=dict()
print('Enter a line of text:')
line=input('')
words=line.split()
print('Words:',words)
print('counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts',counts)
# %%
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names :
    counts[name]=counts.get(name,0)+1
print(counts)
for aaa,bbb in counts.items():
    print(aaa,bbb)
# %%
name=input('Enter file name:')
handle=open(name)
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
# %%
stuff=dict()
print(stuff.get('candy',-1))
# %%
