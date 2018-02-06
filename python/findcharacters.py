'''# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']'''

word_list = ['hello','world','my','name','is','Anna']
testchar = 'o'
new_list=[]
for i in range(0,len(word_list)):
	if word_list[i].find(testchar) != -1:
		new_list.append(word_list[i])   		
print new_list		