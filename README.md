# Zot API
- a bot that scrapes UCI's most recent quarter and gets all available information about classes and their status
- the lambda function runs every 5 minutes——hopefully I don't get billed ;)
- All scraped data is stored in a JSON file and later displayed on AWS

# AWS usage
- go to the link:
- https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/
- remember to load the json before using it!
- Note: some subjects might not have any classes because they aren't offering anything

> ## Search for all courses in a subject:
> - how to get all classes in COMPSCI
> - https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI

> ## Search for a specific course:
> - getting info only on COMPSCI 161:
> - https://1tgg4m2pra.execute-api.us-east-2.amazonaws.com/prod/courses?subject=COMPSCI&id=161

# Flask usage
> ## Dependencies
> - download beautifulsoup ```pip install beautifulsoup4```
> - download flask ```pip install flask```

> ## Run
> ### ```python3 main.py``` on Mac
> ### ```python main.py``` on Windows

> ## Usage
> - Once the server is running open:
> - ```http://127.0.0.1:5000``` or click the server link
> - Once the server is loaded you can now get information on classes
> - ex. ```http://127.0.0.1:5000/compsci``` to get all classes in the subject
> - ex. ```http://127.0.0.1:5000/compsci/computer_graphics``` to get specific class
> - to scrape the quarter again, you must delete the currentTerm.txt file

## All subjects in a list for iteration purposes:
```['AC_ENG', 'AFAM', 'ANATOMY', 'ANESTH', 'ANTHRO', 'ARABIC', 'ARMN', 'ART', 'ART_HIS', 'ARTS', 'ARTSHUM', 'ASIANAM', 'BANA', 'BATS', 'BIO_SCI', 'BIOCHEM', 'BME', 'CAMPREC', 'CBE', 'CBEMS', 'CEM', 'CHC_LAT', 'CHEM', 'CHINESE', 'CLASSIC', 'CLT&THY', 'COGS', 'COM_LIT', 'COMPSCI', 'CRITISM', 'CRM_LAW', 'CSE', 'DANCE', 'DATA', 'DERM', 'DEV_BIO', 'DRAMA', 'E_ASIAN', 'EARTHSS', 'EAS', 'ECO_EVO', 'ECON', 'ECPS', 'ED_AFF', 'EDUC', 'EECS', 'EHS', 'ENGLISH', 'ENGR', 'ENGRCEE', 'ENGRMAE', 'ENGRMSE', 'EPIDEM', 'ER_MED', 'EURO_ST', 'FAM_MED', 'FIN', 'FLM&MDA', 'FRENCH', 'GDIM', 'GEN&SEX', 'GERMAN', 'GLBL_ME', 'GLBLCLT', 'GREEK', 'HEBREW', 'HINDI', 'HISTORY', 'HUMAN', 'HUMARTS', 'I&C_SCI', 'IN4MATX', 'INNO', 'INT_MED', 'INTL_ST', 'IRAN', 'ITALIAN', 'JAPANSE', 'KOREAN', 'LATIN', 'LAW', 'LINGUIS', 'LIT_JRN', 'LPS', 'LSCI', 'M&MG', 'MATH', 'MED', 'MED_ED', 'MED_HUM', 'MGMT', 'MGMT_EP', 'MGMT_FE', 'MGMT_HC', 'MGMTMBA', 'MGMTPHD', 'MIC_BIO', 'MOL_BIO', 'MPAC', 'MSE', 'MUSIC', 'NET_SYS', 'NEURBIO', 'NEUROL', 'NUR_SCI', 'OB_GYN', 'OPHTHAL', 'PATH', 'PED_GEN', 'PEDS', 'PERSIAN', 'PHARM', 'PHILOS', 'PHMD', 'PHRMSCI', 'PHY_SCI', 'PHYSICS', 'PHYSIO', 'PLASTIC', 'PM&R', 'POL_SCI', 'PORTUG', 'PP&D', 'PSCI', 'PSY_BEH', 'PSYCH', 'PUB_POL', 'PUBHLTH', 'RADIO', 'REL_STD', 'ROTC', 'RUSSIAN', 'SOC_SCI', 'SOCECOL', 'SOCIOL', 'SPANISH', 'SPPS', 'STATS', 'SURGERY', 'SWE', 'TAGALOG', 'TOX', 'UCDC', 'UNI_AFF', 'UNI_STU', 'UPPP', 'VIETMSE', 'VIS_STD', 'WRITING']```

## API output for COMPSCI 161

```
{
    "title": "DES&ANALYS OF ALGOR",
    "sections": {
        "34230": {
            "classStatus": "Waitl",
            "classType": "Lec",
            "classSection": "A",
            "classUnits": "4",
            "classInstructors": [
                "SHINDLER, M"
            ],
            "modality": "In-Person",
            "startTime": "10:00",
            "endTime": "10:50",
            "days": [
                "M",
                "W",
                "F"
            ],
            "classLocation": "HIB 100",
            "maxEnrollment": "319",
            "enrolled": "319"
        },
        "34231": {
            "classStatus": "Waitl",
            "classType": "Dis",
            "classSection": "1",
            "classUnits": "0",
            "classInstructors": [
                "SHINDLER, M"
            ],
            "modality": "In-Person",
            "startTime": "5:00",
            "endTime": "5:50p",
            "days": [
                "M",
                "W"
            ],
            "classLocation": "HG 1800",
            "maxEnrollment": "110",
            "enrolled": "110"
        },
        "34232": {
            "classStatus": "Waitl",
            "classType": "Dis",
            "classSection": "2",
            "classUnits": "0",
            "classInstructors": [
                "SHINDLER, M"
            ],
            "modality": "In-Person",
            "startTime": "6:00",
            "endTime": "6:50p",
            "days": [
                "M",
                "W"
            ],
            "classLocation": "HG 1800",
            "maxEnrollment": "110",
            "enrolled": "110"
        },
        "34233": {
            "classStatus": "Waitl",
            "classType": "Dis",
            "classSection": "3",
            "classUnits": "0",
            "classInstructors": [
                "SHINDLER, M"
            ],
            "modality": "In-Person",
            "startTime": "7:00",
            "endTime": "7:50p",
            "days": [
                "M",
                "W"
            ],
            "classLocation": "HG 1800",
            "maxEnrollment": "99",
            "enrolled": "99"
        }
    }
}
  ```

