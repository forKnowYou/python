
import os
import sys
import base64

print(sys.argv)

try:
  if os.path.isfile(sys.argv[1]):
    f = open(sys.argv[1], 'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    
    filename = './temp.txt'
    tempFile = open(filename, 'w')

    f_w = '%s' % ls_f.decode()
    tempFile.write(f_w)
    tempFile.close()
    
    os.system('notepad ' + filename)
    os.remove(filename)
    
except:
  print('path error')
