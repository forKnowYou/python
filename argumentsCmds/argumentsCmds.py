import sys

argv = sys.argv
argc = len(argv)

cmds = []

argumentsMax = "max"

def register(name, description, func, argumentsLen):
  global cmds
  cmds.append([name, description, func, argumentsLen, False])
  
def process():
  global cmds, argc, argv, argumentsMax
  if argc >= 2:
    if argv[1] == "--help":
      print("--help: show this message")
      for i in cmds:
        print(i[0] + ":", i[1])
      exit()
  i = 1
  while i < argc:
    haveCmd = False
    for j in cmds:
      if argv[i] == j[0]:
        if j[4] == True:
          print("repeat command error")
          exit()
        if j[3] == argumentsMax:
          j[2](argv[i + 1 : argc])
          return
        if i + j[3] < argc:
          j[2](argv[i + 1 : i + j[3] + 1])
          i += j[3] + 1
          haveCmd = True
          j[4] = True
          break
        else:
          print("argument error")
          exit()
    if haveCmd == False:
      print("argument error")
      exit()
