# Zot API
- a bot that scrapes UCI's most recent quarter and gets all available information about classes and their status
- All scraped data is stored in a JSON file and later used for a Flask application

# AWS usage
- go to the link:
- https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/

> ## Search for all courses in a subject:
- how to get all classes in COMPSCI
- https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI

> ## Search for a specific course:
- getting info only on COMPSCI 161:
- https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI&id=161

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

## All subjects in list for iteration purposes:
```['AC_ENG', 'AFAM', 'ANATOMY', 'ANESTH', 'ANTHRO', 'ARABIC', 'ARMN', 'ART', 'ART_HIS', 'ARTS', 'ARTSHUM', 'ASIANAM', 'BANA', 'BATS', 'BIO_SCI', 'BIOCHEM', 'BME', 'CAMPREC', 'CBE', 'CBEMS', 'CEM', 'CHC_LAT', 'CHEM', 'CHINESE', 'CLASSIC', 'CLT&THY', 'COGS', 'COM_LIT', 'COMPSCI', 'CRITISM', 'CRM_LAW', 'CSE', 'DANCE', 'DATA', 'DERM', 'DEV_BIO', 'DRAMA', 'E_ASIAN', 'EARTHSS', 'EAS', 'ECO_EVO', 'ECON', 'ECPS', 'ED_AFF', 'EDUC', 'EECS', 'EHS', 'ENGLISH', 'ENGR', 'ENGRCEE', 'ENGRMAE', 'ENGRMSE', 'EPIDEM', 'ER_MED', 'EURO_ST', 'FAM_MED', 'FIN', 'FLM&MDA', 'FRENCH', 'GDIM', 'GEN&SEX', 'GERMAN', 'GLBL_ME', 'GLBLCLT', 'GREEK', 'HEBREW', 'HINDI', 'HISTORY', 'HUMAN', 'HUMARTS', 'I&C_SCI', 'IN4MATX', 'INNO', 'INT_MED', 'INTL_ST', 'IRAN', 'ITALIAN', 'JAPANSE', 'KOREAN', 'LATIN', 'LAW', 'LINGUIS', 'LIT_JRN', 'LPS', 'LSCI', 'M&MG', 'MATH', 'MED', 'MED_ED', 'MED_HUM', 'MGMT', 'MGMT_EP', 'MGMT_FE', 'MGMT_HC', 'MGMTMBA', 'MGMTPHD', 'MIC_BIO', 'MOL_BIO', 'MPAC', 'MSE', 'MUSIC', 'NET_SYS', 'NEURBIO', 'NEUROL', 'NUR_SCI', 'OB_GYN', 'OPHTHAL', 'PATH', 'PED_GEN', 'PEDS', 'PERSIAN', 'PHARM', 'PHILOS', 'PHMD', 'PHRMSCI', 'PHY_SCI', 'PHYSICS', 'PHYSIO', 'PLASTIC', 'PM&R', 'POL_SCI', 'PORTUG', 'PP&D', 'PSCI', 'PSY_BEH', 'PSYCH', 'PUB_POL', 'PUBHLTH', 'RADIO', 'REL_STD', 'ROTC', 'RUSSIAN', 'SOC_SCI', 'SOCECOL', 'SOCIOL', 'SPANISH', 'SPPS', 'STATS', 'SURGERY', 'SWE', 'TAGALOG', 'TOX', 'UCDC', 'UNI_AFF', 'UNI_STU', 'UPPP', 'VIETMSE', 'VIS_STD', 'WRITING']```

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

