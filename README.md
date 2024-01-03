# Zot API
- a bot that scrapes UCI's most recent quarter and gets all available information about classes and their status
- All scraped data is stored in a JSON file and later used for a Flask application

# AWS usage
- go to the link:
- ```[https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/]: (https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/)```

- ## Search for all courses in a subject:
- how to get all classes in COMPSCI
- ```[https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/]: (https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI)```

- ## Search for a specific course:
- getting info only on COMPSCI 161:
- ```[https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI&id=161]: (https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI&id=161)```

# Flask usage
## Dependencies
- download beautifulsoup ```pip install beautifulsoup4```
- download flask ```pip install flask```

## Run
### ```python3 main.py``` on Mac
### ```python main.py``` on Windows

## Usage
- Once the server is running open:
- ```http://127.0.0.1:5000``` or click the server link
- Once the server is loaded you can now get information on classes
- ex. ```http://127.0.0.1:5000/subjects/compsci``` to get all classes in the subject
- ex. ```http://127.0.0.1:5000/subjects/compsci/classes/computer_graphics``` to get specific class

## TODO
- Add more paths
- Get real-time data every time a user searches something
- make code cleaner
- release

## View

```
{
  "ADV_PROG_PROB_SOLV": {
    "codes": {
      "35260": {
        "days": [
          "Tu",
          "Th"
        ],
        "endTime": "4:50p",
        "enrolled": "66",
        "instructors": [
          "KLEFSTAD, R"
        ],
        "location": "HH 178",
        "maxEnrollment": "131",
        "section": "A",
        "startTime": "3:30",
        "status": "OPEN",
        "type": "Lec",
        "units": "4",
        "waitlist": "0"
      },
      "35261": {
        "days": [
          "W"
        ],
        "endTime": "11:50",
        "enrolled": "66",
        "instructors": [
          "MOHADDESI, S",
          "KLEFSTAD, R"
        ],
        "location": "HG 1800",
        "maxEnrollment": "131",
        "section": "1",
        "startTime": "11:00",
        "status": "OPEN",
        "type": "Lab",
        "units": "0",
        "waitlist": "0"
      }
    },
    "title": "CompSci 253P"
    ...
}
  ```

