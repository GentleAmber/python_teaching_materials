class NewInt(int):

  def __hash__(self):
    return 2 * super().__hash__() # super().<方法名>是在调用父类的该方法

a = NewInt(3)
b = int(3) # == b = 3
print(f"For NewInt a 3, hash(a) = {hash(a)}")
print(f"For NewInt a 3, a == 3 is {a == 3}. a == 6 is {a == 6}")
print(f"For int b 3, hash(b) = {hash(b)}")
print(f"For int b 3, b == 3 is {b == 3}")
