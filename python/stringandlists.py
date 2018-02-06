words = "It's thanksgiving day. It's my birthday,too!"
print words.index("day")
my_str=''
my_str=words.replace('day','month')
print my_str

x = [2,54,-2,7,12,98]
min(x)
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
a=x[0]
b=x[len(x)-1]
print a,b
print[a,b]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y=x[:len(x)/2]
print y
z=x[len(x)/2:]
z.insert(0,y)
print z
