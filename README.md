# Zot API
- a bot that scrapes UCI's most recent quarter and gets all available information about classes and their status
- All scraped data is stored in a JSON file and later used for a Flask application

# dependencies
- download beautifulsoup ```pip install beautifulsoup4```
- download flask ```pip install flask```

# Run
### ```python3 main.py``` on Mac
### ```python main.py``` on Windows

# Usage
- Once the server is running open:
- ```http://127.0.0.1:5000``` or click the server link
- Once the server is loaded you can now get information on classes
- ex. ```http://127.0.0.1:5000/subjects/compsci```
- ex. ```http://127.0.0.1:5000/subjects/compsci/classes/computer_graphics```

# View

```{
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
  }```
