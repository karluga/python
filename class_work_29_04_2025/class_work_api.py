import urllib.request
import json

def get_fruits_by_name(family_name):
    url = f"https://fruityvice.com/api/fruit/family/{family_name}"

    with urllib.request.urlopen(url) as response:
        data = response.read()
        fruits = json.loads(data)
        for fruit in fruits:
            print(f"Name: {fruit['name']}, Calories: {fruit['nutritions']['calories']}")

family_name = "Rosaceae"
get_fruits_by_name(family_name)
