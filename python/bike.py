class Bike(object):
	def __init__(self,max_speed,price):
		self.price=price
		self.max_speed=max_speed
		self.miles=0
	def displayinfo(self):
		print "bike's price is",self.price
		print "maximum speed is",self.max_speed,"mph"
		print "total miles is",self.miles,"miles"
	def ride(self):
		print "Riding"
		self.miles += 10
	def reverse(self):
		print "Reversing"
		if self.miles >= 5 :
			self.miles=self.miles-5

bike1 = Bike(100, 15)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(150, 20)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(180, 30)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()

