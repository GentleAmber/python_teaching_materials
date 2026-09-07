import os

class AgeError(Exception):
  pass

print(f"该进程的pid为：{os.getpid()}")

while (True):
  age = input("请输入你的年龄：")
  try:
    age_num = int(age)
    if (age_num > 120 or age_num <= 0):
      raise AgeError("年龄不合法。请重新输入。")
    break
  except ValueError:
    print("非整数，请重新输入。")
  except AgeError as e:
    print(e)