name=input('Enter your name:')
print('your name has ',len(name),'places')
n=int(input('Which position do you want to print?:'))
print('The letter associated to the ',n,' position is ',name[n-1])
rp=input('Find how many times a letter is repeated across your name:')
count=0
for letter in name:
    if letter==rp:
        count=count+1
print('The letter',rp,' is repeated',count,' times.')
for letter in name:
    print(letter)

# CLASE 2 HOW TO MANIPULATE STRINGS
#CONCATENATE A STRING
a=input('Enter your name:')
b=input('Enter your last name:')
c=a+' '+b
print('Your name is',c)
#in OPERATOR TO FIND VALUES IN STRINGS
'rp' in name
if rp in name:
    print('Found it!')
# STRING COMPARISON
#can use == to compare strings
# cambiar a minusculas
name2=name.lower()#Cambia a minusculas
name3=name2.capitalize()# primera letra en mayuscula
name3_1=name2.upper()#Cambia todo a mayusculas
name4=name.find('i') #Encontrar la posición de la variable en el arreglo
# si no lo encuentra la salida es un "-1"
print(name2)
print(name3)
print(name3_1)
print(name4)
#Buscar y reemplazar
name5=name.replace('uis','aspero')
print (name5)

#PARSING AND EXTRACTING
data='Cualquier información desde luchernandezse@unal.edu.co o por celular'
atpos=data.find('@')
print(atpos)
sppos=data.find(' ',atpos)#buscar el siguiente espacio luego de atpos
print(sppos)
host=data[atpos+1:sppos] #[a:b] desde la posicion a hasta uno antes de la posicion b
# [a:] a partir de a hasta el final
# [:b] desde el inicio hasta la posición b
print (host)