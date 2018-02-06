X='hi i am new to python'
Y='HI I AM SINDHU'
#capitalizing letters string.capitalize()-Capitalize the first character
print X.capitalize()
#output:Hi i am new to python

#upper-make all characters uppercase-string.upper()
print X.upper()
#output:HI I AM NEW TO PYTHON

#lower-make all characters lowercase-string.lower()
print Y.lower()	
#output:hi i am sindhu

#count-returns the number of occurences of substring in string
print X.count('o')
#output:2

#find-returns the index of the start of the first occurence of substring within string
print X.find('new')
#output:8

#index-It determines if string str occurs in string or in a substring of string if starting index beg and ending index end are given. This method is same as find(), but raises an exception if sub is not found.
print X.index('new',5)
print X.find('new',10)
#output:8
#output:-1


#split-returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
print X.split()
print X.split('a')
#output:['hi', 'i', 'am', 'new', 'to', 'python']
#output:['hi i ', 'm new to python']

#join-returns a string that is all strings within our set (in this case a list) concatenated.
music = ["Abba","Rolling Stones","Black Sabbath","Metallica"]
print '1'.join(music)
print ''.join(music)
print '\n'.join(music)
#output:Abba1Rolling Stones1Black Sabbath1Metallica
#output:AbbaRolling StonesBlack SabbathMetallica
#output:Abba
#       Rolling Stones
#       Black Sabbath
#       Metallica

#replace-The method replace() returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
#Syntax
#Following is the syntax for replace() method 
#str.replace(old, new[, max])
print X.replace('hi', 'bye')
#output:bye i am new to python
print X.replace('i', 'bye',1)
#output:hbye i am new to python

#format-format() method takes any number of parameters. But, is divided into two types of parameters:
#Positional parameters - list of parameters that can be accessed with index of parameter inside curly braces {index}
#Keyword parameters - list of parameters of type key=value, that can be accessed with key of parameter inside curly braces {key}

print("Hello I'm {0} {1}and {2}{3}").format("hi", "i", "am", "new to python")
#output:Hello I'm hi i and am new to python

X="'hi i am new to python.{}'"
print(X.format("I am sindhu"))
#output:'hi i am new to python.I am sindhu'


#LIST

#len-gives the length of the list
ninjas = ['Rozen', 'KB', 'Oliver']
print len(ninjas)
#output:3

#max-returns item from the list with max value
abc=[23,45,67]
print max(ninjas)
print max(abc)
#output:Rozen
#output:67

print min(ninjas)
print min(abc)
#output:KB
#output:23

#index-

print ninjas.index('KB')
#output:1

#append-
ninjas.append(123)
print ninjas
#output:['Rozen', 'KB', 'Oliver', 123]

#pop-
print ninjas.pop()
#output:123
print ninjas
#output:['Rozen', 'KB', 'Oliver']

#remove-This method does not return any value but removes the given object from the list.
ninjas.remove('KB')
print ninjas
#OUTPUT:['Rozen', 'Oliver']

#insert-The method insert() inserts object obj into list at offset index.
#Syntax
#Following is the syntax for insert() method 
#list.insert(index, obj)
ninjas.insert(1,123)
print ninjas
#output:['Rozen', 123, 'Oliver']

#sort-sorts object of the list
ninjas.sort()
print ninjas
#output:[123, 'Oliver', 'Rozen']
ninjas.sort(reverse=True)
print ninjas
#output:['Rozen', 'Oliver', 123]

#reverse
ninjas.reverse()
print ninjas
#output: [123, 'Oliver', 'Rozen']

#extend-The method extend() appends the contents of seq to list.
ninjas = ['Rozen', 'KB', 'Oliver']
dojo=['abc','def']
ninjas.extend(dojo)
print ninjas
#output :['Rozen', 'KB', 'Oliver', 'abc', 'def']


