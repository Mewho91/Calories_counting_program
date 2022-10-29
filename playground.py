from pprint import pprint
import json


class Playground:
    import requests
    # ________________________________________read requests
    SHEET_ENDPOINT = "https://api.sheety.co/39c535bbf835a3ced3a84cfc3061120f/caloriesProgram/arkusz1"

    response = requests.get(url=SHEET_ENDPOINT)
    data = response.json()
    # chicken_cals = data["arkusz1"][0]["testCals"]
    # beef_cals = data["arkusz1"][1]["testCals"]
    len_of_names = len(data["arkusz1"])
    # print(data["arkusz1"][0])
    # # kurwa jest ___________________________________________________ wyszukiwanie kalorii po nazwie
    # for _ in range(0, len_of_names):
    #     if data["arkusz1"][_]["testName"] == "Kurczak":
    #         print(data["arkusz1"][_]["testCals"])
    #


    def name_chose(self):
        self.names =[]
        for name in range(0, self.len_of_names):
            self.names.append(self.data["arkusz1"][name]["testName"])
        return self.names

    def data_by_name(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.cal = float(self.data["arkusz1"][_]["testCals"]) * prod_gram
                self.protein = float(self.data["arkusz1"][_]["protein"]) * prod_gram
                self.carbo = float(self.data["arkusz1"][_]["carbo"]) * prod_gram
                self.fat = float(self.data["arkusz1"][_]["fat"]) * prod_gram
            return f"cal {self.cal}, prot {self.protein}, carbo {self.carbo}, fat {self.fat}"

    def count_calories(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.cal = float(self.data["arkusz1"][_]["testCals"]) * prod_gram
        return self.cal
    def count_protein(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.protein = float(self.data["arkusz1"][_]["protein"]) * prod_gram
        return self.protein
    def count_carb(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.carbo = float(self.data["arkusz1"][_]["carbo"]) * prod_gram
        return self.carbo
    def count_fat(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.fat = float(self.data["arkusz1"][_]["fat"]) * prod_gram
        return self.fat

    # if chicken_name == "Kurczak":
    #     print(chicken_cals)
    # else : pass

    # {'arkusz1': [{'testName': 'Kurczak', 'testCals': 1000, 'id': 2}, {'testName': 'Wołowina', 'testCals': 2000, 'id': 3}]}
    # ____________________________________________________