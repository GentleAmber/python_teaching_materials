class HashTest:

  def __init__(self, strValue):
    self.strValue = strValue

  def __eq__(self, other) -> bool:
    if (str(self.strValue) == str(other.strValue)):
      return True
    else:
      return False

  def __hash__(self):
    return 1
  
  def __repr__(self):
    return "HashTest(" + str(self.strValue) + ")"

he1 = HashTest("hello")
he2 = HashTest("hello")
cat = HashTest("cat")

# d = {he1: 1, he2: 2, cat: 3}
# print(d)
