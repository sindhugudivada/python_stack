class Call(object):
	def __init__(self,id,name,phoneno,time,reason):
		self.id = id
		self.name = name
		self.phoneno = phoneno
		self.time = time
		self.reason = reason
	def display(self):
		print self.id
		print self.name
		print self.phoneno
		print self.time
		print self.reason
		return self 
class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = 0
	def add(self, caller):
		self.calls.append(caller)
		self.queue_size += 1
		return self

	def remove(self):
		self.calls.pop(0)
		self.queue_size -= 1
		return self

	def info(self):
		print "length of the queue", self.queue_size
		for count in self.calls:
			print "caller:", count.name
			print "number:", count.phoneno
			print "call time:", count.time
			print "reason to call:", count.reason	
		return self 
caller1 = Call(1,"sindhu","831-840-7899","7:00 pm","Juan solo")
caller2 = Call(2,"vineel","831-840-7780","12:00 am","I am a God")
caller3 = Call(3,"mounica","309-222-7777","6:00 AM","morning call")
callcenter1 = CallCenter()
callcenter1.add(caller1).add(caller2).add(caller3).info().remove().info()        
