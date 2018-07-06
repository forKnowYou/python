import time
import pythoncom
import thread
import sys

import pyHook
import win32api
import win32con

leftClickEnable = False

def leftClickTask(threadName, delay):
  global leftClickEnable
  while leftClickEnable:
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.09)
  print "thread over"

def onMouseEvent(event): 
    global leftClickEnable
    
    print "MessageName:",event.MessageName
    print "Message:", event.Message
    print "Time:", event.Time
    print "WindowName:", event.WindowName     
    print "Position:", event.Position  
    print "---"
    
    if event.Message == 519:
      if leftClickEnable == False:
        print "start_new_thread leftClickTask"
        leftClickEnable = True
        thread.start_new_thread(leftClickTask, ("thread-1", 1,))
      return False
    if event.Message == 520:
      print "leftClickTask stop"
      leftClickEnable = False

    return True

def main():     
    hm = pyHook.HookManager()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()
    
if __name__ == "__main__":
    main()
    