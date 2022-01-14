class MyClass:
  def __init__(self, name, age):
    self.attribute1 = value1
    self.attribute2 = value2

def myfunc(self):
  print("Hello my attrib1 is " + self.attribute1)

#p1 = MyClass()
#p1.myfunc()
#print(p1.attribute1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()