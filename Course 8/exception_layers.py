class B_EXC(Exception):
  pass

class C_EXC(B_EXC):
  pass

for cls in [B_EXC, C_EXC]:
    try:
        raise cls()
    except C_EXC:
        print("C_EXC")
    except B_EXC:
        print("B_EXC")
    except Exception:
        print("Exception")
    