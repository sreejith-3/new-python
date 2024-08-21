class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname


#Use the Person class to create an object, and then execute the printname method:

p1 = Person("John", "Mathew")
print(p1.fname)
print(p1.lname)