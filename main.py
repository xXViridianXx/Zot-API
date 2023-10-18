from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import threading
import os
from  scraper import *
import json

app = Flask(__name__)

allCourses = None

scheduler = BackgroundScheduler()

FILENAME = 'scrapedQuarter.json'
TERMFILE = 'currentTerm.txt'

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

def updateZOTAPI(FILENAME, TERMFILE):


    createFile(TERMFILE)
        
    lastTerm = readTerm(TERMFILE)

    url = 'https://www.reg.uci.edu/perl/WebSoc'
    soup = requestPage(url)

    termField = getTermFields(soup)

    currentTerm = getTerm(termField)
    print(currentTerm, lastTerm)

    if lastTerm != currentTerm:
        print(f"Term was changed, now scrapping...")
        print(f"Please wait, scrapping a lot of data")
        departmentField = getDepartmentFields(soup)
        departments = getDepartment(departmentField)
        
        AllCourses = scrapePages(departments, currentTerm, url)

        writeTerm(TERMFILE, currentTerm)
        createJsonFile(AllCourses, FILENAME)

def runApp(FILENAME, TERMFILE):
    global allCourses
    updateZOTAPI(FILENAME, TERMFILE)
    allCourses = loadJson(FILENAME)
    app.run(debug=True)

@app.route('/')
def Home():
     return "Welcome to UCI's Current Courses API"

@app.route("/<subject>")
def getSubject(subject):
        global allCourses
        subject = subject.upper()
        if subject in allCourses:
            return allCourses[subject], 200
        return f'Error: Searched for {subject} but nothing was found. Please check spelling', 400
       
@app.route("/<subject>/<classname>") 
def getClass(subject, classname):
   global allCourses
   subject = getSubject(subject)
   classname = classname.upper()

   if subject[1] != 200:
        return subject[0]
   if classname in subject[0]:
        return subject[0][classname], 200
   return f'Error: Searched for {subject} {classname} but nothing was found. Please check spelling', 400


if __name__ == "__main__":
     runApp(FILENAME, TERMFILE)