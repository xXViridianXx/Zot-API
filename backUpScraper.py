import requests
from time import *
from bs4 import BeautifulSoup
from random import randint
import json

# request websoc page
def requestPage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# get all departments
def getDepartmentFields(soup):
    departmentField = soup.find('select', {'name': 'Dept'})
    return departmentField

# find all term fields
def getTermFields(soup):
    termField = soup.find('select', {'name': 'YearTerm'})
    return termField

# get the department
def getDepartment(departmentField):
    department = [option['value']
                  for option in departmentField.find_all('option')]
    return department


# get the current term
def getTerm(termField):
    option = termField.find('option')
    return option['value']


# gets the list of days the class is available
# if the character it lands on is u or h
# that means the previous char was a T
# combine those strings and append to stack
def getDays(dayString):
    stack = []
    for i in dayString:
        day = i
        if i == 'u' or i == 'h':
            char = stack.pop()
            day = char + i
        stack.append(day)
    return stack


# returns a list of length 2
# the first index: startTime
# last index: endTime
def getTimes(timeString):
    timeList = timeString.split('-')
    return timeList

# function to get the final
# can't scrape final with Beautifulsoup
def getFinal(finalString):
    pass

# returns delay so bot doesn't get denied requests
def getDelayedTime():
    delay = randint(2, 5)
    return delay

# splits a string and joins based on seperator
def parseAndJoin(givenString, splitter, separator):
    splitString = givenString.split(splitter)
    joinedString = separator.join(splitString)
    return [joinedString, len(splitString)]

# removes labels at end of list
def removeEndLabel(classHeaderInfo, label):
    if classHeaderInfo[-1] == label:
        classHeaderInfo.pop()
    return classHeaderInfo

# gets the class names and title
# returns None if fails
def getClassNames(firstChar, cache, subjectLength):
    classNames = None
    classNumber = 2 if subjectLength > 1 else 1

    if firstChar.isalpha():
        cache = removeEndLabel(cache, '(Prerequisites)')
        # courseTitle = '_'.join([cache[0], cache[classNumber]])
        courseTitle = cache[classNumber]
        # print(cache)
        courseName = ' '.join(cache[index] for index in range(classNumber+1, len(cache)))
        classNames = (courseTitle, courseName)
    return classNames

# set variables for courses
def storeRowContent(tableData):

    # data in form of
    # [classStatus, classCode, classType, classSection, classUnits, classInstructors
    # ,startTime, endTime, days, classLocation, maxEnrollment, enrolled, waitlist]
    rowContent = []
    for i in range(-1, 10):
        if i == 4:
            instructors = parseTeachers(tableData, i, '.') 
            rowContent.append(instructors)
        elif i == 5:
            when = stripAndSplit(getTableDataText(tableData, 5))
            rowContent.extend(getClassTimes(when))
        elif i == 8:
            enrolled = splitTableData(tableData, i, '/')[0]
            rowContent.append(enrolled)
        else:

            columnData = getTableDataText(tableData, i)
            rowContent.append(columnData)
    
    return rowContent


def getRowContentData(rowContent, i):
    return rowContent[i]

# not add classCode to ht because code will serve as the key
# the value of the code will be a dictionary
# ht[0] was classStatus
# but ht[1] was class code, just removed it when adding to ht
def setAllSectionsInfo(sections, rowContent):
    keys = ['classType', 'classSection', 'classUnits', 'classInstructors',
     'startTime', 'endTime', 'days', 'classLocation', 'maxEnrollment', 'enrolled', 'waitlist']
    
    classStatus = getRowContentData(rowContent, 0)
    setKeyValue('classStatus', classStatus, sections)

    for i in range(2, len(rowContent)):
        key = keys[i-2]
        data = getRowContentData(rowContent, i)
        setKeyValue(key, data, sections)

# strips and splits a string
def stripAndSplit(item):
    return item.strip().split()

# deteremines if table data is class names or info
def isClassName(item, subjectLength):
    cache = stripAndSplit(item.text)
    firstChar = cache[0]
    firstString = firstChar[0]
    classNames = getClassNames(firstString, cache, subjectLength)
    return classNames

# returns just the strign containg the time
def parseTime(when):
    timeString = ''
    if (len(when) > 2):
        timeString = ''.join([when[1], when[2]])
    else:
        timeString = when[1]
    return timeString

# gets class times
# or makes everything TBA if counlt find
# some times represented as 1
# some times are split
def getClassTimes(when):
    startTime, endTime = '', ''
    if(len(when) > 1):
        timeString = parseTime(when)
        times = getTimes(timeString)
        startTime, endTime = times[0], times[1]
        days = getDays(when[0])
    else:
        startTime, endTime = ['TBA'], ['TBA']
        days = ['TBA'] 
    
    return (startTime, endTime, days)
            

# gets an index of tableData list
def getTableDataText(tableData, index):
    return tableData[index].text

# splits the tableData text using a seperator
# removes last string if empty
def splitTableData(tableData, index, seperator):
    splitDataString = getTableDataText(tableData, index)
    splitDataString = splitDataString.split(seperator)
    return splitDataString

# removes last empty string if split
def removeEmptyString(splitString):
    if splitString[-1] == '':
        splitString.pop()
    return splitString


# some teachers showed with STAFFTeacher
# with no space in between so this function fixes that
# similar to splitTableData expect check for STAFF
def parseTeachers(tableData, index, seperator):
    splitDataString = splitTableData(tableData, index, seperator)
    splitDataString = removeEmptyString(splitDataString)
    substring = splitDataString[0]
    checkFor = 'STAFF'
    if checkFor in substring and len(substring) > 5:
        splitDataString[0] = substring[5:]

    return splitDataString


 
def setFormRequests(currentTerm, department):
    return { 'YearTerm': currentTerm, 'Dept': department}

def setKeyValue(key, value, hastable):
    hastable[key] = value

# Function to scrape each page with respective course listings
# based on department
def scrapePages(departments, currentTerm, url):
    allCourses = {}
    
    # Ignoring All because form won't load
    for i in range(1, len(departments)):
        # the form information to request
        coursesInfo = {}
        courses = {}
        classes = {}
        data = setFormRequests(currentTerm, departments[i])

        # getting response from url an inputing request data in form
        response = requests.post(url, data=data)

        # check if response successful
        if response.status_code != 200:
            continue
            
        result_soup = BeautifulSoup(response.text, 'html.parser')

        # getting container with courses
        courseList = result_soup.find('div', {'class': 'course-list'})

        # selecting all table rows with valign top 
        # because that's where important data is
        tableRows = courseList.find_all('tr', {'valign': 'top'})

        tableData = None

        subjectData = parseAndJoin(departments[i], ' ', '_')
        subject = subjectData[0]

        if '/' in subject:
            splitString =  subject.split('/')
            subject = '_'.join(splitString)

        subjectLength = subjectData[1]

        courseTitle = ''
        courseName = ''
        for i in tableRows:

            classNames = isClassName(i, subjectLength)
            if classNames:
                courseTitle, courseName = classNames[0], classNames[1]
                coursesInfo = {}
                classes = {}
                continue

            coursesInfo['title'] = courseName
            sections = {}
            tableData = i.find_all('td')
            rowContent = storeRowContent(tableData)
            code = getRowContentData(rowContent, 1)

            setAllSectionsInfo(sections, rowContent)

            setKeyValue(code, sections, classes)
            setKeyValue('sections', classes, coursesInfo)
            setKeyValue(courseTitle, coursesInfo, courses)

        print(f'scraped {subject}')

        setKeyValue(subject, courses, allCourses)

        sleep(getDelayedTime())

    return allCourses


def createJsonFile(data, file):
    with open(file, "w") as json_file:
        json.dump(data, json_file)
