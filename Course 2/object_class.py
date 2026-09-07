# 这里使用售票亭

class TicketBooth:
  # 类属性。所有对象共享。此处为总票池
  totalTicket = 100

  # 初始化对象用的函数=构造器。所有规定在这里面的属性为对象属性，仅属于
  # 创建的对象。只能命名为__init__
  def __init__(self, id, name = 'default'):
    self.id = id
    self.name = name

  # 类函数sellTicket：从总票池中卖掉num张票
  @classmethod
  def sellTicket(cls, num):
    cls.totalTicket -= num

  # 对象函数changeId：修改单个票亭的id编号
  def changeId(self, id):
    self.id = id


ticketBooth1 = TicketBooth(1)
ticketBooth2 = TicketBooth(2)
print(f"修建了票亭{ticketBooth1.id}号和票亭{ticketBooth2.id}号")

ticketBooth1.sellTicket(3)
ticketBooth2.sellTicket(4)
print(f"票亭{ticketBooth1.id}号卖掉了3张票\n"
f"票亭{ticketBooth2.id}号卖掉了4张票")
print(f"现在总票数还剩下：{ticketBooth1.totalTicket}")

# 用python的逻辑运算再来判断下两个对象是否共享了一个类属性
print(ticketBooth1.totalTicket == ticketBooth2.totalTicket)
# 确认两个对象的类属性都指向了同一块内存
print(ticketBooth1.totalTicket is ticketBooth2.totalTicket)

# 改变其中一个对象的id。检查两个对象的id是否保持独立
ticketBooth1.changeId(4)
print(f"ticketBooth1为票亭{ticketBooth1.id}号")
print(f"ticketBooth2为票亭{ticketBooth2.id}号")

# 类方法、类属性也可以直接被类调用。无需非得创建对象
TicketBooth.sellTicket(3)
print(f"无论如何，卖出了3张票")

print(f"现在总票数还剩下：{TicketBooth.totalTicket}")
