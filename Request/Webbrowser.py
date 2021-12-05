#----------------------------------------------
Study request function with json format
#----------------------------------------------

import requests
import json
import pprint

"min": 15,
"user_type": "registered"
}

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    pprint.pprint(questions)

    for question in questions["items"]:
        webbrowser.open_new["link"]
        webbrowser
import webbrowser
import webbrowser
params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": "2019-08-20",
    "tagged": "python",
