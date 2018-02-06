class animal(object):
     '''count=0'''
     def __init__(self,name,health=150):
        self.name=name
	self.health=health
	'''animal.count+=1'''
      def walk(self):
          self.health=self.health-1
          return self
      def run(self):
          self.health=self.health-5
          return self
      def displayhealth(self):
          print " health is",self.health
animal12=animal('cow')
animal12.walk()
animal12.run()
animal12.run()
animal12.displayhealth()

class Dog(animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
        
    def pet(self):
        self.health += 5
        return self

dog = Dog('Odie')
dog.walk().walk().walk().run().run().pet().displayhealth()

class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayhealth(self):
        print "This is a dragon"
        super(dragon, self).displayhealth()

dragon1 = dragon('trackdog')
dragon1.fly().displayhealth()


