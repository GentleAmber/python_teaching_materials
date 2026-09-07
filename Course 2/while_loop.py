# while循环比较普通，唯一值得一提的是else也可以用在while块里，
# else: 里的语句块仅在while循环执行完时执行。常用于判断循环
# 是否被中止。或用于做一些仅当循环结束时做的事情

i = 1

while i <= 5:
  print(i)
  i += 1

  if (i == 3):
    break
else:
  print("while循环正常退出")