from  scraper import *
from helpers import *
import boto3


def runMaster():
    s3 = boto3.client('s3')

    FILENAME = 'scrapedSubjects.json'
    bucket = 'class-subjects-data'
    url = 'https://www.reg.uci.edu/perl/WebSoc'

    soup = requestPage(url)

    departmentField = getDepartmentFields(soup)
    departments = getDepartment(departmentField)

    termField = getTermFields(soup)

    currentTerm = getTerm(termField)
    
    # converting to bytes for encoding
    dataStream = bytes(json.dumps(departments).encode('UTF-8'))

    s3.put_object(Bucket=bucket, Key=FILENAME, Body=dataStream)


def lambda_handler(event, context):
    runMaster()

if __name__ == "__main__":
    lambda_handler('test', 'test')
