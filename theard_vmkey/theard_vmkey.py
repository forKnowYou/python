import psutil
import time
import sys
import pykeyboard
from pykeyboard import PyKeyboard
import platform
import pythoncom

if platform.system() != 'Windows':
  print('not support other system except windows now')
  exit()
  
import win32
import pyHook

from makeconfigjson import MakeConfigJSON

print(sys.argv)

conf = MakeConfigJSON('config.json')

if len(sys.argv) == 3:
  print('use argv config')
  processName = sys.argv[1]
  vmKey = sys.argv[2]
else:
  print('use last config')
  processName = conf.getKey('lastProcess')
  vmKey = conf.getKey('lastVMKey')
  
listenKeys = conf.getKey('listenKeys')
print(processName)
print(vmKey)
print(listenKeys)

if processName == None or vmKey == None or listenKeys == None:
  print('argv error')
  exit()

def onKeyBoardEvent(e):s
  print(dir(e))
  return True
  
while True:
  time.sleep(0.005)
  hm = pyHook.HookManager()
  hm.KeyDown = onKeyBoardEvent
  hm.HookKeyboard()
  pythoncom.PumpMessages()
  # get all theard pids
  pids = psutil.pids()
  for i in pids:
    process = psutil.Process(i)
    try: 
      if process.name().upper().index(processName.upper()) != -1:
        #print(process.status())
        pass
    except:
      pass
