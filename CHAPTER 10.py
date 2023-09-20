#%%
#TUPLES
x=('Glenn','Sally','Joseph')
print(x[2])
y=(1,9,2)
print(y)
print(max(y))
#Truple no se pueden modificar luego de ser definidos.
#Listas y strings si son modificables.
#No deja modificar ni organizar ni alterar el tuple
#Solo tiene dos funciones asociadas.
#Permite que el programa sea mas eficiente ahorrando memoria.
#Cuando se tienen variables constantes se usan en forma de tuples.
# Asignacion simultanea:
(x,z)=(4,'fred')
(a,b)=(99,max(y)*2)
print(b)
print(a)
#comparacion tuples
#compara el primer elemento, si hay similitud hace el segundo ETC
#Lo mismo con letras y numeros por igual.
print((0,1,2)<(5,3,2))
print (y)
print(('Andres','Sam')>('Andres','San'))
#Se pueden organizar por el primer termino, luego el segundo etc.
# Se puede pasar de diccionario a tupple
d={'a':10,'b':1,'c':22}
print(d.items())
print(sorted(d.items()))
#El key del dictionario es unico asiq ue permite ser organizado facilmente.
#organizacion por key
for k,v in sorted(d.items()):
    print(k,v)
#Es mas dificil organizar por valores un diccionario
# Se reorganiza el diccionario en un tupple (value,key) y se organiza por valor
#empleando un ciclo for
tmp=list()
for k,v in d.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp,reverse=False)
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)
# encontrar las diez palabras mas comunes.
name=('romeo.txt')
handle=open(name)
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for k,v in counts.items():
    newtup=(v,k) #Crear una lista de tupples
    lst.append(newtup)
lst=sorted(lst,reverse=True)
for v,k in lst[0:10]:
    print(k,v)
# %%
x,y=3,4

# %%
print(x)
print(y)
# %%
