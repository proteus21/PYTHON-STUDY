#------------------------------------------------
#Downloading data from server
# 1) use request function,
# 2) downloading datas and values from site
# 3) verify correct format
# 4) check who win
#-----------------------------------------------
import requests
import json


r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    return completedTaskFrequencyByUser

def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]

def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
   completedTaskFrequencyByUser = count_task_frequency(tasks)
   usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
   print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o id: ",
   usersWithTopCompletedTasks)
