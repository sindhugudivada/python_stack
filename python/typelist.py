l = ['magical unicorns',19,'hello',98.98,'world']
'''
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98" '''
def typelist(l):
	str1=""
	count=0
	for element in l:
		checktype=type(element)
		if checktype is str:
			str1=str1+element	
		elif checktype is int or checktype is float:
			count=count+element
	print "string:"+str1		
	print "sum:"+str(count)
typelist(l)	


'''
def typelist_version_2(l):
	str1=""
	count=0
	for element in l:
		checktype=type(element)
		if checktype is str and int:
			print("The list you entered is of mixed type")
		if checktype is str:
			str1=str1+element	
		elif checktype is int:
			count = count + element
	print str1,
	print count,
typelist_version_2(l)	
'''				
			
