def assign_1_to_x(x):
  x = 1
  
  def this_is_a_local_function():
    pass

  print(x)

x = 5
assign_1_to_x(x)
print(x)

def create_y():
  y = 5 
  global z
  z = "global z"
  return y

print(create_y())
print("This is z: " + z)
