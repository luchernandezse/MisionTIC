fname2=input('Enter File Name:  ')
try:
    fhand=open(fname2)#sE VERIFICA QUE EL NOMBRE DEL ARCHIVO EXISTA
except:
    print('File Cannot be oppened: ',fname2)
for line in fhand:
    line=line.rstrip()
    inp=line.upper()
    print(inp)