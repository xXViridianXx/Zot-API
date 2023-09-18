from flask import Flask, request, jsonify
import os
from  scraper import *

app = Flask(__name__)


@app.route('/')
def Home():
     return "Welcome to UCI's Current Courses API"
if __name__ == "__main__":

    PATH = '/Users/aniketpratap/Desktop/Github/AutoEnroller'
    FILENAME = 'scrapedQuarter.json'

    lastTerm = ''

    if not os.path.exists('currentTerm.txt'):
         with open('currentTerm.txt', 'w') as file:
            pass
        
    with open('currentTerm.txt', 'r') as file:
            lastTerm = file.read()
    
    url = 'https://www.reg.uci.edu/perl/WebSoc'
    soup = requestPage(url)

    termField = getTermFields(soup)

    currentTerm = getTerm(termField)

    if os.path.exists('currentTerm.txt') and lastTerm != currentTerm:
        print(f"Term was changed, now scrapping...")
        print(f"Please wait, scrapping a lot of data")
        departmentField = getDepartmentFields(soup)
        departments = getDepartment(departmentField)
        with open('currentTerm.txt', 'w') as file:
            file.write(currentTerm)
        AllCourses = scrapePages(departments, currentTerm, url)

        createJsonFile(AllCourses)
    
    app.run(debug=True)