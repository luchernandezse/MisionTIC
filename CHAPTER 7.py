xtext=open('FILES_HANDLE.txt')
count=0
for line1 in xtext:
    line1=line1.rstrip()
    print (line1)
    count=count+1
print('Line Count:',count)
# LEER LA TOTALIDAD DEL ARICHIVO
fhand=open('FILES_HANDLE.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])
#leer del principio hasta el caracter 20-1 del archivo de texto.
#Buscar alguna palabra guía en el archivo e imprimir la linea de dicha palabra.
fhand=open('FILES_HANDLE.txt')
for line in fhand:
    line=line.rstrip()#Este comando quita el ultimo \n colocado cada vez que lee una linea y todo sale pegado.
    if line.startswith('From:') :
        print(line)
fhand=open('FILES_HANDLE.txt')
for line in fhand:
    line=line.rstrip()#Este comando quita el ultimo \n colocado cada vez que lee una linea y todo sale pegado.
    if not line.startswith('From:') : # El ifnot es un condicional para buscar lineas que no cumplan un requisito dado. 
        continue #saltar lineas en las que no estamos interesados
    print(line)
fhand=open('FILES_HANDLE.txt')
for line in fhand:
    line=line.rstrip()#Este comando quita el ultimo \n colocado cada vez que lee una linea y todo sale pegado.
    if not '@unal.edu.co' in line : # busca la condicion en un arreglo y si no se cumple salta la linea
        continue 
    print(line)


fname2=input('Enter File Name:  ')
try:
    fhand=open(fname2)#sE VERIFICA QUE EL NOMBRE DEL ARCHIVO EXISTA
except:
    print('File Cannot be oppened: ',fname2)
count=0
for line in fhand:
    if line.startswith('Subject'):
        count=count+1
print('There were',count,'subject lines in',fname2)
        
