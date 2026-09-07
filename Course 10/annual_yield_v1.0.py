# 该模块包括系统相关的形参和函数。
# 文档：https://docs.python.org/3.14/library/sys.html
import sys
import os
import re

# sys.argv以只读list形式存储所有传入的参数。这里把参数赋给argv方便后面打字
argv = sys.argv
script_name = os.path.basename(__file__)

# 有传参
if (len(argv) >= 2):
  # 传参含-h或--help，显示帮助信息
  if ("-h" in argv or "--help" in argv):
    print("\n=========== 年化收益率计算工具v1.0 ===========")
    print("----------- 帮助信息 -----------")
    print("-p： 阶段涨幅。需要输入百分号之前的数字。例如对于阶段涨幅40.9%的产品，输入40.9而非0.409。")
    print("-y: 阶段持续年数。例如对于过去2年的阶段涨幅，输入2。如果没有输入则默认为0。")
    print("-d：阶段持续天数。例如对于过去2年又40天的阶段涨幅，在该旗帜后输入40。如果没有输入则默认为0。")
    print(f"""示例：计算一个在2年又40天内阶段涨幅40.9%的产品的年化收益：
          python {script_name} -p 40.9 -y 2 -d 40\n""")
  
  # 否则传参为功能传参。进行对应处理
  else:
    # 去除脚本名新建list args，用以遍历取出参数
    args = argv[1:]
    i = 0
    args_dict = {'-p': None, '-y': None, '-d': None}
    illegal = False

    while (i < len(args)):
      # 当前i指向一个合法旗帜，且后面有跟参数
      if (args[i] in args_dict and i + 1 < len(args)):
        # 判断参数是否是数字。是的话转换成数字格式后存入args_dict并把i置于该旗帜-参数组之后
        if (re.match(r'^-?\d+(\.\d+)?$', args[i + 1])):
          args_dict[args[i]] = float(args[i + 1])
          i += 2
        else:
          print(f"旗帜{args[i]}的参数不存在或不合法。")
          illegal = True
          break
      # 当前i指向一个合法旗帜，但后面没有参数且处于列表的最后一位（i+1>=len(args))
      elif (args[i] in args_dict):
        print(f"旗帜{args[i]}缺少参数。")
        illegal = True
        break
      # i没有指向合法旗帜，说明出现了不合法旗帜或者没有旗帜的数字
      else:
        print("旗帜不合法或没有旗帜。")
        illegal = True
    
    for key in args_dict:
      if (args_dict[key] is None):
        if (key == '-p'):
          illegal = True
        else:
          args_dict[key] = 0
      else:
        if (key != '-p' and args_dict[key] < 0):
          print(f"{key}的参数不得小于0。")
          illegal = True
        
    
    if (illegal): 
      exit()

    base = 1 + args_dict['-p']/100
    power = 365 / (365 * args_dict['-y'] + args_dict['-d'])
    annual_yield = pow(base, power) - 1
    print(f"对于过去{args_dict['-y']}年{args_dict['-d']}天，阶段涨幅为{args_dict['-p']}的产品而言：")
    print(f"年化收益率为：{round(annual_yield * 100,2)}%")

# 无传参。显示程序简介。
elif (len(argv) == 1):
  print(f'这是一个年化收益率计算工具。启动时请输入 "python {script_name} -h" 或者 "python {script_name} --help" 获取帮助信息。')