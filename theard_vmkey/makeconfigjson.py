import json

class MakeConfigJSON:
  
  def __init__(self, fileName):
    self.fileName = fileName
    self.f = open(fileName, 'r+')
    self.jsonStr = self.f.read()
    try:
      self.data = json.loads(self.jsonStr)
    except:
      self.data = [{}]
    self.f.close()
    print(self.data)
    
  def getKey(self, keyName):
    return self.data[0].get(keyName)
    
  def save(self):
    self.f = open(self.fileName, 'w+')
    self.f.write(json.dumps(self.data))
    self.f.close()
    
  def setKey(self, keyName, keyData):
    self.data[0][keyName] = keyData
