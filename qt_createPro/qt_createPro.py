import sys
sys.path.append("..")
if sys.version_info.major < 3:
  print("not support python2")
  exit()
print(sys.argv)

import re
import os

import argumentsCmds.argumentsCmds as argCmds

resourcesPath = ""
libraryPath = ""
defines = []
rslt = ""

def appExit(reason):
  print(reason)
  exit()

def handleResourcesPath(argv):
  global resourcesPath
  if os.path.isdir(argv[0]) == False:
    appExit("resources path error")
  else:
    resourcesPath = argv[0]

def handleLibraryPath(argv):
  global libraryPath
  if os.path.isdir(argv[0]) == False:
    appExit("library path error")
  else:
    libraryPath = argv[0]

def handleLibraryFromLibs(argv):
  global libraryPath, defines, rslt
  fileName = "./qt_createPro_libs.txt"
  if os.path.exists(fileName):
    f = open(fileName)
    r = f.readline()
    while r != "":
      if re.match("platform: \S*, lib: \S*, defines: \S*", r):
        l = r.split(",")
        l[0] = l[0].replace("platform: ", "").lower()
        l[1] = l[1].replace(" lib: ", "")
        l[2] = l[2].replace(" defines: ", "").split(" ")
        if l[0].find(argv[0].lower()) >= 0:
          if os.path.isdir(l[1]):
            libraryPath = l[1]
          if l[2][0] != "null":
            rslt += "DEFINES += \\\n"
            for i in l[2]:
              if i != "":
                rslt += "  " + i.replace("\r", "").replace("\n", "").replace("\t", "") + " \\\n"
            break
      r = f.readline()
    if libraryPath == "":
      print("canot find lib from qt_createPro_libs.txt or format error")
  else:
    print("canot find qt_createPro_libs.txt, app will create it, type --help for more info")
    f = open(fileName, "w")
    f.close()
  
argCmds.register("-r", "project resources path", 
  handleResourcesPath, 1)
argCmds.register("-l", "project library path", 
  handleLibraryPath, 1)
argCmds.register("-lf", "project library and DEFINES from qt_createPro_libs.txt, format(xx can be null): \nplatform: xx, lib: xx, defines: xx xx", 
  handleLibraryFromLibs, 1)

argCmds.process()

createPro = open("./qt_createPro.txt", "w")

if libraryPath != "":
  files = os.walk(libraryPath)
  rslt += "\nINCLUDEPATH += \\\n"
  for dirpath, dirnames, filenames in files:
    for i in filenames:
      if re.search("\.h$", i) != None or re.search("\.hpp$", i) != None:
        if rslt.count(dirpath) == 0:
          rslt += "  " + dirpath + " \\\n"
  files = os.walk(libraryPath)
  rslt += "\nRESOURCES += \\\n"
  for dirpath, dirnames, filenames in files:
    for i in filenames:
      if re.search("\.c$", i) != None or re.search("\.cpp$", i) != None or re.search("\.ino$", i) != None:
        rslt += "  " + dirpath + "\\" + i + " \\\n"

if resourcesPath != "":
  files = os.walk(resourcesPath)
  rslt += "\nHEADERS += \\\n"
  for dirpath, dirnames, filenames in files:
    for i in filenames:
      if (re.search("\.h$", i) != None) or (re.search("\.hpp$", i) != None):
        rslt += "  " + dirpath + "\\" + i + " \\\n"
        
  files = os.walk(resourcesPath)        
  rslt += "\nSOURCES += \\\n"
  for dirpath, dirnames, filenames in files:
    for i in filenames:
      if (re.search("\.c$", i) != None) or (re.search("\.cpp$", i) != None) or (re.search("\.ino$", i) != None):
        rslt += "  " + dirpath + "\\" + i + " \\\n"

print(rslt)

createPro.write(rslt)
createPro.close()

os.system("notepad " + "./qt_createPro.txt")
