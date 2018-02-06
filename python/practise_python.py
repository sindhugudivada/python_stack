sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

arr=[sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]
checktype=type(arr)

def testdata(arr):

	for element in arr:
		checktype = type(element)
		if checktype is int:
			if element >=100:
				print "larger number"
			else:
				print "smaller number"
		elif checktype is str:
			if len(element) >=50:
				print "Long Sentence"
			else:
				print "short sentence"	
		elif checktype is list:
			if len(element) >= 10:
				print "Big List"
			else:
				print "short List"	
testdata(arr)	


	
		
