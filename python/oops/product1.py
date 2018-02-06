class product(object):
  def __init__(self,price,item_name,weight,brand,status):
    self.price=price
    self.item_name=item_name
    self.weight=weight
    self.brand=brand
    self.status=status
  def sell(self):
    self.status="sold"
  def addtax(self,tax):
    self.price=self.price+tax
  def Return(reason):  
    if reason is "defective":
      print "defective"
      print "price is 0"
    elif reason is "new":
      print "for sale"
    elif reason is "opened":
      print "used"
      price = price-0.2(price)
  def display_info(self):
    print self.price
    print self.item_name
    print self.weight
    print self.brand
    print self.status
    
product1=product(100,'maker',20,'calphalon','opened')
product1.addtax(0.20)
product1.Return()
product1.display_info()