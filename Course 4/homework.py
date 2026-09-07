class Animal:
  def run(self):
    print("Animal is running")
  def act(self):
    print("Not defined")

class Turtoise(Animal):
  def act(self):
    print("往前爬一步")

class Rabbit(Animal):
  def act(self):
    print("往前跳一步")

def run_twice(animal):
  animal.run()
  animal.run()

run_twice(Animal())

def act(animal):
  animal.act()


Rabbit().act()
Turtoise().act()

