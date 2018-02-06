'''Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A'''


import random
def scores(num):
  print "Scores and Grades"
  for i in range(0,num):
    scores = random.randint(60,100)
    if scores>=60 and scores<70:
      print "Score:" ,scores,";Your grade is D"
    elif scores>=70 and scores<79:
      print "Score:" ,scores,";Your grade is C"
    elif scores>=80 and scores<89:
      print "Score:" ,scores,";Your grade is B"
    else:
      print "Score:" ,scores,";Your grade is A"  
scores(10)           
