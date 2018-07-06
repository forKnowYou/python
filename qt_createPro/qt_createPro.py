import os
import sys
import re

print(sys.argv)

try:
  if os.path.isdir(sys.argv[1]) or os.path.isdir(sys.argv[2]):
    filename = './qt_createPro.txt'
    createPro = open(filename, 'w')
    rslt = ''
    
    if os.path.isdir(sys.argv[1]):
      rslt += 'INCLUDEPATH += \\\n'
      files = os.walk(sys.argv[1])
      for dirpath, dirnames, filenames in files:
        for i in filenames:
          if (re.search('\.h$', i) != None) or (re.search('\.hpp$', i) != None):
            if rslt.count(dirpath) == 0:
              rslt += '  ' + dirpath + ' \\\n'

    if os.path.isdir(sys.argv[2]):
      files = os.walk(sys.argv[2])
      for dirpath, dirnames, filenames in files:
        for i in filenames:
          if (re.search('\.h$', i) != None) or (re.search('\.hpp$', i) != None):
            if rslt.count(dirpath) == 0:
              rslt += '  ' + dirpath + ' \\\n'
              
      rslt += '\nHEADERS += \\\n'
      files = os.walk(sys.argv[2])
      for dirpath, dirnames, filenames in files:
        for i in filenames:
          if (re.search('\.h$', i) != None) or (re.search('\.hpp$', i) != None):
            rslt += '  ' + dirpath + '\\' + i + ' \\\n'
              
      rslt += '\nSOURCES += \\\n'
      files = os.walk(sys.argv[2])
      for dirpath, dirnames, filenames in files:
        for i in filenames:
          if (re.search('\.c$', i) != None) or (re.search('\.cpp$', i) != None) or (re.search('\.ino$', i) != None):
            rslt += '  ' + dirpath + '\\' + i + ' \\\n'

    print(rslt)

    createPro.write(rslt)
    createPro.close()

    os.system('notepad ' + filename)
    os.remove(filename)
  
except:
  print('path error')
