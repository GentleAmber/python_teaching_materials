# 表示用户信息错误的异常
class UserInfoError(Exception):
  pass

# 录入用户出生年份
try:
  year = int(input("请输入你的出生年份："))
  if (year < 1990 or year > 2026):
    raise UserInfoError(f"出生年份应该介于1990到2026之间。你输入了{year}")
except ValueError:
  raise # 此处为了演示更重要的部分，处理这个异常不重要。因此直接把异常抛出，不进行处理
except UserInfoError as e: 
  print(e)
  # def __str__(self):
  #   return super().__str__() * 2
  print("在演示软件里就先不处理了。继续往下吧")


# 录入用户出生月份
try:
  month = int(input("请输入你的出生月份："))
  if (month <= 0 or month > 12):
    raise UserInfoError("出生月份应该介于1到12之间")  
except ValueError:
  raise
except UserInfoError: 
  raise # 此处演示一下直接抛出自定义异常看起来是怎样的

