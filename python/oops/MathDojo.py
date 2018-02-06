class MathDojo(object):
  def __init__(self):
    self.result=0
  def add(self,*args):
    for i in args:
      if type(i) == list or type(i) == tuple:
        for j in range(0,i): 
          self.result=self.result+ j
      elif type(i)==int:
        self.result=self.result+ i
    return self    
  def subtract(self,*args):
    for i in args:
      if type(i) ==list or type(i) ==tuple:
        for j in range(0,i): 
          self.result=self.result-j
      elif type(i)==int:
        self.result=self.result- i
    return self 
  
md=MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
