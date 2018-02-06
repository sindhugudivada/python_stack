import random
random_num = random.random()
def tosses(num):
  print "starting the program..."
  count=0
  count1=0
  for i in range(0,num+1):
    x=random.random()
    x_rounded = round(x)
    if x_rounded == 0: 
      count=count+1
      print "Attempt #",i,": Throwing a coin... It's a head! ... Got",count,"head(s) so far and",count1,"tail(s) so far" 
    else:
      count1=count1+1
      print "Attempt #",i,": Throwing a coin... It's a tail! ... Got",count,"head(s) so far and",count1,"tail(s) so far" 
tosses(30)

