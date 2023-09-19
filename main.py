from flask import Flask, request, jsonify
import os
from  scraper import *
import json

app = Flask(__name__)

allCourses = None

def loadJson():
        with open('scrapedQuarter.json', 'r') as file:
            return json.load(file)
        

def createFile(file):
     if not os.path.exists(file):
         
         with open(file, 'w') as f:
            pass
         
def readTerm(file):
         with open('currentTerm.txt', 'r') as f:
            return f.read()
         
def writeTerm(file, currentTerm):
     with open(file, 'w') as f:
            f.write(currentTerm) 

@app.route('/')
def Home():
     return "Welcome to UCI's Current Courses API"

@app.route("/subjects/<subject>")

def getSubject(subject):
        global allCourses
        subject = subject.upper()
         
        if subject in allCourses:
            return allCourses[subject], 200
        return f'Error: Searched for {subject} but nothing was found. Please check spelling', 400



        
@app.route("/subjects/<subject>/classes/<classname>") 
def getClass(subject, classname):
   
   subject = subject.upper()
   classname = classname.upper()

   with open('scrapedQuarter.json', 'r') as file:
        allCourses = json.load(file)

        courseSubject = allCourses[subject]
        if classname in courseSubject:
            return courseSubject[classname], 200
        return f'Error: Searched for {subject}/{classname} but nothing was found. Please check spelling', 400


if __name__ == "__main__":

    PATH = '/Users/aniketpratap/Desktop/Github/AutoEnroller'
    FILENAME = 'scrapedQuarter.json'
    TERMFILE = 'currentTerm.txt'

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
        createJsonFile(AllCourses)

    allCourses = loadJson()

    app.run(debug=True)