import requests
import enum





class Data(enum.Enum):
    CALORIES = "testCals"
    CARBS = "carbo"
    PROT = "protein"
    FAT = "fat"


class Functions:

    SHEET_ENDPOINT = "https://api.sheety.co/39c535bbf835a3ced3a84cfc3061120f/caloriesProgram/arkusz1"
    response = requests.get(url=SHEET_ENDPOINT)
    data = response.json()
    len_of_names = len(data["arkusz1"])

    def name_chose(self):
        self.names =[]
        for name in range(0, self.len_of_names):
            self.names.append(self.data["arkusz1"][name]["testName"])
        return self.names

    def count(self, prod_input, prod_gram, c_name):
        counted = 0
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                counted = float(self.data["arkusz1"][_][c_name]) * prod_gram
        return round(counted, 2)

    def sum_of_all_meals(self, d):
        self.sum_cal = []
        self.sum_prot = []
        self.sum_carb = []
        self.sum_fat = []
        for key in d:
            self.sum_cal.append(d[key]['Cal'])
            self.sum_prot.append(d[key]['prot'])
            self.sum_carb.append(d[key]['carb'])
            self.sum_fat.append(d[key]['fat'])

        return f"Summary calories: {round(sum(self.sum_cal), 2)}, Summary proteins: {round(sum(self.sum_prot), 2)}, " \
               f"Summary carbohydrates: {round(sum(self.sum_carb),2)}" \
               f"Summary fat: {round(sum(self.sum_fat), 2)}"
