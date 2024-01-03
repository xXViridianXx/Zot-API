from  scraper import *
from helpers import *
from child import *
import boto3

url = 'https://www.reg.uci.edu/perl/WebSoc'
s3 = boto3.client('s3')

# write data to s3
def writeS3(bucket, FILENAME, data):

    try:
        s3.put_object(Bucket=bucket, Key=FILENAME, Body=json.dumps(data))
    except Exception as e:
        print('failed write to s3')

# init s3 bucket for scraped classes
def initS3(bucket, FILENAME):
    initS3 = {}
    writeS3(bucket, FILENAME, initS3)

# invokes child process to run
def runChildLambda(eventData, childFunctionARN):
    lambdaClient = boto3.client('lambda')

    response = lambdaClient.invoke(
        FunctionName=childFunctionARN,
        InvocationType='RequestResponse',  
        Payload=json.dumps(eventData)
    )
    return response

def runMaster():
    # s3 = boto3.client('s3')

    # FILENAME = 'scrapedSubjects.json'
    # bucket = 'class-subjects-data'

    soup = requestPage(url)

    departmentField = getDepartmentFields(soup)
    departments = getDepartment(departmentField)

    termField = getTermFields(soup)

    currentTerm = getTerm(termField)
    return [departments, currentTerm]

    # converting to bytes for encoding
    # dataStream = bytes(json.dumps(departments).encode('UTF-8'))

    # s3.put_object(Bucket=bucket, Key=FILENAME, Body=dataStream)


def lambda_handler(event, context):
    bucket = 'class-subjects-data'
    FILENAME = 'scrapedSubjects.json'

    if not event:
        # master process
        departments, currentTerm = runMaster()

        childFunctionARN = 0

        # start at 1 to skip "ALL" option
        for i in range(1, len(departments)):
            eventData = {'department': departments[i], 'term': currentTerm, 'url': url}
            runChildLambda(eventData, childFunctionARN)

    else:

        department = event.get('department')
        term = event.get('term')

        if not department:
            print(f'Error getting info for {department}')
            return
        
        writeS3(bucket, FILENAME, scrapedClasses)
        runChild(department, term, url)
        


if __name__ == "__main__":
    lambda_handler('test', 'test')
