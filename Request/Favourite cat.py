#----------------------------
# file json, request function,
# verify which cat is the favourite
#----------------------------
import json
import credentials
import requests


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Incorrect format", response.text)
    else:
        return content


def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params,
                     )

    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers=credentials.headers)

    return get_json_content_from_response(r)


print("Hey, login - enter login and password")
# get login and password
# Check if login and password is correct
# login successful
# get the userId and name from the database

userId = "agh2m"
name = "Arkadiusz"

print("Hello " + name)
favouriteCats = get_favourite_cats(userId)
print("Your favourite cats are ", favouriteCats)
randomCat = get_random_cat()
print("The cat was drawn: ", randomCat[0]['url'])


