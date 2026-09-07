# 先演示单独处理一个简单异常
# def this_will_fail():
#   num * 3

# try:
#   this_will_fail()
# except NameError as err: # 新引入：这里的...as <变量名>使你之后可以用<变量名>指代异常
# # 也可以写except Exception ... 但是从你知道的最小范围的子类开始写有利于知道具体问题，是个好习惯
#   print(f"发现NameError异常：{err}")



# 然后演示一个接近实际生产的例子
while True:
  user_input = input("请输入一个整数：")

  try:
    num = int(user_input)
    print(f"你输入的整数是：{num}。谢谢配合。")
    break
  except ValueError:
    print("错误。请重新输入")
  # finally:
  #   print("finally执行了")


# 最后演示一下finally的用法
# user_input = input("请输入一个整数：")
# try:
#   num = int(user_input)
#   print(f"你输入的整数是：{num}。")
# except ValueError:
#   print("错误。")
# finally:
#   print("谢谢。再见")