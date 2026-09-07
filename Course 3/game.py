import random
# 随机数对应表。0、1、2分别对应石头、剪刀、布
gestures = ["石头", "剪刀", "布"] #gestures[0]

class Player:
  def shoot(self):
    rand_int = random.randint(0,2)
    gesture = gestures[rand_int]
    print(f"玩家{self.num}出了{gesture}")
    return rand_int

  def __init__(self, num):
    self.num = num

def play(player1, player2):
  rand_int1 = player1.shoot()
  rand_int2 = player2.shoot()

  # 两个玩家出的一样：平局
  if (rand_int2 == rand_int1):
    result = 0
  # 当两个玩家出的不一样时，如果玩家1出石头：
  elif (rand_int1 == 0):
    # 玩家2出剪刀的话，玩家2赢，否则玩家1赢
    if (rand_int2 == 1):
      result = 2
    else:
      result = 1
  # 如果玩家1出剪刀：
  elif (rand_int1 == 1):
    # 玩家2出石头，玩家2赢，否则玩家1赢
    if (rand_int2 == 0):
      result = 2
    else:
      result = 1
  # 如果玩家1出布：
  else: 
    # 下略
    if (rand_int2 == 0):
      result = 1
    else: 
      result = 2

  if (result == 0):
    print("平局了，继续玩！")
    play(player1, player2)
  elif (result == 1):
    print(f"玩家{player1.num}赢了！")
  else:
    print(f"玩家{player2.num}赢了！")
    
player1 = Player(1)
player2 = Player(2)
play(player1, player2)