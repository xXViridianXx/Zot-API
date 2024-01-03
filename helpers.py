import json

def loadJson(file):
        with open(file, 'r') as f:
            return json.load(f)
        

def createFile(file):
     if not os.path.exists(file):
         with open(file, 'w') as f:
            pass
         
def readTerm(file):
         with open(file, 'r') as f:
            return f.read()
         
def writeTerm(file, currentTerm):
     with open(file, 'w') as f:
            f.write(currentTerm) 