import requests
from time import *
from bs4 import BeautifulSoup
from random import randint
url = 'https://www.reg.uci.edu/perl/WebSoc'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

departmentField = soup.find('select', {'name': 'Dept'})

termField = soup.find('select', {'name': 'YearTerm'})


def getDepartment(departmentField):
    department = [option['value']
                  for option in departmentField.find_all('option')]
    return department


def getTerm(termField):
    option = termField.find('option')
    return option['value']


departments = getDepartment(departmentField)

currentTerm = getTerm(termField)

total = len(departments)
count = 0
# for department in departments:

x = randint(2, 5)


for i in departments:
    if i == 'COMPSCI':
        break
    count +=1
data = {
    'YearTerm': currentTerm,
    'Dept': departments[count]
}


ht = {}
response = requests.post(url, data=data)
if response.status_code == 200:
    # Parse the HTML content of the response for further processing
    result_soup = BeautifulSoup(response.text, 'html.parser')

    G = result_soup.find('div', {'class': 'course-list'})

    B = G.find_all('tr', {'bgcolor': '#fff0ff'})

    for i in B:
        # print(i)
        bruh = i.find('td', {'class': 'CourseTitle'})
        cache = bruh.text.strip().split()
        if cache[-1] == '(Prerequisites)':
            cache.pop()
        for i in cache:
            courseName = ' '.join([cache[0], cache[1]])
            courseTitle = ' '.join(cache[index] for index in range(2, len(cache)))
            
            ht[courseName] = courseTitle
    # print(f'passesd for: {department}')

    # count +=1
    # Extract and process the result data as needed
else:
    print('Failed to retrieve the page for: ', departments[1])
for i in ht:
    print(i)
sleep(x)

# print(f'passed for {count}/ {total} test cases')
# for i in departments:
#     print(i)
