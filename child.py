

from  scraper import *
import json

allCourses = None

FILENAME = 'scrapedQuarter.json'

# def loadJson(file):
#         with open(file, 'r') as f:
#             return json.load(f)
        

# def createFile(file):
#      if not os.path.exists(file):
#          with open(file, 'w') as f:
#             pass
         
# def readTerm(file):
#          with open(file, 'r') as f:
#             return f.read()
         
# def writeTerm(file, currentTerm):
#      with open(file, 'w') as f:
#             f.write(currentTerm) 

def runChild(department, currentTerm, url):
    departmentName = f'{department}.json'    
    scrapedCourseData = scrapePages(department, currentTerm, url)

    createJsonFile(scrapedCourseData, departmentName)


def lambda_handler(event, context):
    department = event['department']
    currentTerm = event['currentTerm']
    url = event['url']

    runChild(department, currentTerm, url)

# if __name__ == "__main__":
#     lambda_handler('test', 'test')