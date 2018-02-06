class Car(object):
  def __init__(self,price,speed,fuel,mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    if price > 10000:
      self.tax = 0.15
    else:
      self.tax = 0.12
  def display_all(self):
    print "price:",self.price
    print "speed:",self.speed
    print "fuel:",self.fuel 
    print "mileage:",self.mileage
    print "tax:",self.tax 		

car1=Car(5000,200,'Full',15)
car1.display_all( )


