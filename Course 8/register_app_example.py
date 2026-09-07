# 录入用户出生年份
try:
  year = int(input("请输入你的出生年份："))
except ValueError:
  raise # 此处为了演示更重要的部分，处理这个异常不重要。因此直接把异常抛出，程序员不进行处理

if (year < 1990 or year > 2026):
  print("出生年份应该介于1990到2026之间")
  exit()

# 录入用户出生月份
try:
  month = int(input("请输入你的出生月份："))
except ValueError:
  raise

if (month <= 0 or month > 12):
  print("出生月份应该介于1到12之间")
  exit()

# 录入用户出生日期
try:
  day = int(input("请输入你的出生日期："))
except ValueError:
  raise

if (day <= 0 or day > 31):
  print("出生日期应该介于1到31之间")
  exit()
