class Dog:

  def __init__(self, name):
    self.name = name

  def bark(self): # 改掉参数名也一样成立
    print(f"Woof, {self.name}")

  @classmethod 
  def eat(cls):
    print("eat")
    
ivy = Dog("Ivy")
ivy.bark() # Python做的：Dog.bark(ivy)

Dog.bark(ivy)

