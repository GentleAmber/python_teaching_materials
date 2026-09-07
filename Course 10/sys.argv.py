import sys
argv = sys.argv

if (len(argv) > 0):
  print(f"存储参数使用的数据类型为：{type(argv)}\n参数：{", ".join(argv)}\n参数个数：{len(argv)}\n第0位参数：{argv[0]}")