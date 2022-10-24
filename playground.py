import requests


# ________________________________________read requests
SHEET_ENDPOINT = "https://api.sheety.co/39c535bbf835a3ced3a84cfc3061120f/caloriesProgram/arkusz1"

response = requests.get(url=SHEET_ENDPOINT)
data = response.json()
chicken_cals = data["arkusz1"][0]["testCals"]
beef_cals = data["arkusz1"][1]["testCals"]


chicken_name = data["arkusz1"][0]["testName"]

if chicken_name == "Kurczak":
    print(chicken_cals)
else : pass

# {'arkusz1': [{'testName': 'Kurczak', 'testCals': 1000, 'id': 2}, {'testName': 'Wołowina', 'testCals': 2000, 'id': 3}]}
# ____________________________________________________