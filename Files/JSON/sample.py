import json


students = [
    {
        'is_start': True,
        'name': 'Bob',
        'surname': 'Bobenko',
        'marks': {
            'Python': 85.3,
            'math': 90,
            'English': 50
        }
    },
    {
        'name': 'Alex',
        'surname': 'Alexich',
        'marks': {
            'Python': 12.3,
            'math': 34,
            'English': 53
        }
    },
    {
        'name': 'Alina',
        'surname': 'Kirenko',
        'marks': {
            'Python': 43.3,
            'math': 53,
            'English': 93
        }
    }
]

string = json.dumps(students, indent=4)
print(string)
obj = json.loads(string)
