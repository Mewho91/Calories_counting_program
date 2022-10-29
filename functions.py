import requests


class Functions:
    # ________________________________________read requests
    SHEET_ENDPOINT = "https://api.sheety.co/39c535bbf835a3ced3a84cfc3061120f/caloriesProgram/arkusz1"

    response = requests.get(url=SHEET_ENDPOINT)
    data = response.json()
    len_of_names = len(data["arkusz1"])

    def name_chose(self):
        self.names =[]
        for name in range(0, self.len_of_names):
            self.names.append(self.data["arkusz1"][name]["testName"])
        return self.names

    def count_calories(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.cal = float(self.data["arkusz1"][_]["testCals"]) * prod_gram
        return round(self.cal, 2)

    def count_protein(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.protein = float(self.data["arkusz1"][_]["protein"]) * prod_gram
        return round(self.protein, 2)

    def count_carb(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.carbo = float(self.data["arkusz1"][_]["carbo"]) * prod_gram
        return round(self.carbo, 2)

    def count_fat(self, prod_input, prod_gram):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                self.fat = float(self.data["arkusz1"][_]["fat"]) * prod_gram
        return round(self.fat, 2)

    def sum_of_all_meals(self, dict):
        self.sum_cal = []
        self.sum_prot = []
        self.sum_carb = []
        self.sum_fat = []
        for key in dict:
            self.sum_cal.append(dict[key]['Cal'])
            self.sum_prot.append(dict[key]['prot'])
            self.sum_carb.append(dict[key]['carb'])
            self.sum_fat.append(dict[key]['fat'])

        return f"Summary calories : {(sum(self.sum_cal))}, Summary proteins : {(sum(self.sum_prot))}, " \
               f"Summary carbohydrates : {(sum(self.sum_carb))}" \
               f"Summary fat : {(sum(self.sum_fat))}"
