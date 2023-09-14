import requests
from time import *
from bs4 import BeautifulSoup
from random import randint
url = 'https://catalogue.uci.edu/allcourses/'

response = requests.get(url)
text = response.content
# print(text)

soup = BeautifulSoup(text, "html.parser")

# print(soup.prettify())

mainContainer = soup.find('main')
courseContainer = mainContainer.find('div', id='atozindex')
courses = courseContainer.find_all('li')


# adds char if alphabet else turn into '_'
def addCharacter(character, subtab):
    # if character.isalpha():
        # subtab.append(character.lower())

    # else:
        subtab.append(character)


# builds a list of sub directories to lopo through websites
def buildSubjectTab(course):
    courseTitle = course.text
    index = courseTitle.find('(') + 1
    subtab = []
    while courseTitle[index] != ')':
        character = courseTitle[index]
        addCharacter(character, subtab)
        index += 1
    return ''.join(subtab)


# creates subTabs list

def buildSubTabsList(subjectTabs):
    for course in courses:
        tab = buildSubjectTab(course)
        subjectTabs.append(tab)


def buildUrls(subjectTabs, subjectPages):
    for subject in subjectTabs:

        subjectUrl = ''.join([url, subject])
        subjectPages.append(subjectUrl)
    return subjectPages


subjectPages = []

subjectTabs = []

# buildSubTabsList(subjectTabs)

for i in subjectTabs:
     print(i)
# for 
# pageUrls = buildUrls(subjectTabs, subjectPages)
# header = {"User-Agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.{random.randrange(1000)} (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
#           }
# for i in pageUrls:
#     response = requests.get(i)

#     x = randint(2, 5)

#     passed = 'passed' if response.status_code == 200 else 'failed'
#     print(f'{passed} {i} ')
#     sleep(x)
