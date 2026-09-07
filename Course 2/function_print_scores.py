class Student:
  def __init__(self, cn, math, en):
    self.cn = cn
    self.math = math
    self.en = en

students = [Student(95, 98, 100), Student(40, 50, 20), Student(87, 64, 90)]

# no function
# for student in students:
#   print(student.cn)
#   print(student.math)
#   print(student.en)
#   print(student.biology)
#   print(student.geography)
#   print(student.chemical)
#   print(student.biology)
#  # ...

# with function
def printScore(student):
  print(student.cn)
  print(student.math)
  print(student.en)

for student in students:
  printScore(student)


