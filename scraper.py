import requests
from time import *
from bs4 import BeautifulSoup
from random import randint
import json

def requestPage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def getDepartmentFields(soup):
    departmentField = soup.find('select', {'name': 'Dept'})
    return departmentField

def getTermFields(soup):
    termField = soup.find('select', {'name': 'YearTerm'})
    return termField


def getDepartment(departmentField):
    department = [option['value']
                  for option in departmentField.find_all('option')]
    return department


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


def getTimes(timeString):

    timeList = timeString.split('-')

    return timeList


def getFinal(finalString):
    pass



def scrapePages(departments, currentTerm, url):

    count = 1

    AllCourses = {}
    
    for i in range(1, len(departments)):

        x = randint(2, 5)

        data = {
            'YearTerm': currentTerm,
            'Dept': departments[i]        }

        coursesInfo = {}
        courses = {}
        classes = {}

        print(departments[i])
        response = requests.post(url, data=data)
        if response.status_code == 200:
            # Parse the HTML content of the response for further processing
            result_soup = BeautifulSoup(response.text, 'html.parser')

            courseList = result_soup.find('div', {'class': 'course-list'})

            tableRows = courseList.find_all('tr', {'valign': 'top'})

            tableData = None

            subjectSplit = departments[i].split()
            subject = '_'.join(subjectSplit)

            for i in tableRows:
                cache = i.text.strip().split()

                firstItem = cache[0]
                if firstItem[0].isalpha():

                    coursesInfo = {}
                    if cache[-1] == '(Prerequisites)':
                        cache.pop()
                    for i in cache:
                        courseTitle = ' '.join([cache[0], cache[1]])
                        courseName = '_'.join(cache[index]
                                            for index in range(2, len(cache)))
                    coursesInfo['title'] = courseTitle
                    # print(courseName)
                    classes = {}

                else:
                    codes = {}
                    tableData = i.find_all('td')

                    code = tableData[0].text
                    type = tableData[1].text

                    # print(f'code: {code}, type: {type}')
                    section = tableData[2].text
                    units = tableData[3].text
                    instructors = tableData[4].text.split('.')
                    when = tableData[5].text.strip().split()
                    place = tableData[6].text
                    maxEnrollment = tableData[7].text
                    enrolled = tableData[8].text.split('/')[0]
                    waitlist = tableData[9].text
                    status = tableData[-1].text

                    if(len(when) > 1):

                        timeString = ''
                        startTime, endTime = '', ''
                        if (len(when) > 2):
                            timeString = ''.join([when[1], when[2]])
                        else:
                            timeString = when[1]
                        times = getTimes(timeString)
                        startTime, endTime = times[0], times[1]
                        days = getDays(when[0])
                    else:
                        startTime, endTime = ['TBA'], ['TBA']
                        days = ['TBA']

                    if instructors[-1] == '':
                        instructors.pop()

                    codes['type'] = type
                    codes['section'] = section
                    codes['units'] = units
                    classes[code] = codes
                    codes['instructors'] = instructors
                    codes['days'] = days
                    codes['startTime'] = startTime
                    codes['endTime'] = endTime
                    codes['location'] = place
                    codes['maxEnrollment'] = maxEnrollment
                    codes['enrolled'] = enrolled
                    codes['waitlist'] = waitlist
                    codes['status'] = status

                    coursesInfo['codes'] = classes

                    courses[courseName] = coursesInfo

            count += 1
            # Extract and process the result data as needed
        else:
            print('Failed to retrieve the page for: ', departments[1])
        
        print(f'Finished {subject}')
        AllCourses[subject] = courses

        sleep(x)

    return AllCourses


def createJsonFile(AllCourses):
    fileName = "scrapedQuarter.json"

    with open(fileName, "w") as json_file:
        json.dump(AllCourses, json_file)
