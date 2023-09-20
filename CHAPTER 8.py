#lists
#LESSON 1
friends=['Joseph','Glenn','Sally']
print(friends[2]) #Looking inside lists
#CHANGE LISTS
#str are not mutuable, thats why we have .lower() functions
lotto=[2,14,15,16]
print(lotto)
lotto[1]=20
print(lotto)
#LENGHT
print(len(friends[0]))
print(len(lotto))
#RANGE: mostly when we are constructing a loop
#extract a part of a list
print(len(friends))
print(range(len(friends)))
print(range(4))
#COUNTING LOOP USING RANGE
for i in range(len(friends)):
    friend=friends[i]
    print('HNY: ',friend)

#LESSON 2
#CONCATENATE
a=[1,2,3]
b=[4,5,6]
c=a+b
print (c)
#SLICED LISTS
print(c[1:3])
print(c[:4])
print(c[3:])
print(c[:])
#OTHER OPERATORS
x=list()
print(type(x))
print(dir(x))
#BUILD A LIST
stuff=list()
stuff.append('book')
stuff.append('99')
print(stuff)
stuff.append('cookie')
print(stuff)
#list stays in order and new elements are added at the end of the list
#FIND VALUES
print('book' in stuff)
print('99' in stuff)
print('5' in c)
15 in stuff
#LIST IN ORDER
friends.sort()
print(friends)
#BUILT-IN FUNCTIONS
print(sum(c))
print(max(c))
print(min(c))
print(sum(c)/len(c))

#LESSON 3 LIST AND STRING WORKING TOGETHER
#split
abc='Miguel Angel Hernández'
stuff2=abc.split()
print(stuff2)
print(len(stuff2))
print(stuff2[0])
#split divides for spaces.
#the user can specify the split parameter:
line='A  lot   of   spaces'
etc=line.split()
print(etc)
line='A;Lot;Of;Spaces'
thing=line.split()
print(thing)
thing=line.split(';')
print(thing)
#FIND A TEXT IN AN EMAIL
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue 
    print(line)
    words2=line.split()
    print(words2)
#DOUBLE SPLIT
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue 
    words2=line.split()
    email=words2[1]
    #print(email)
    pieces=email.split('@')
    print(pieces[0])
