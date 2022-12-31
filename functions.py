import requests
import enum


def how_many_meals(max_meals, min_meals):
    is_ok = True
    while is_ok:
        user_input = int(input("Select how many meals do you want to count? \n"))
        if user_input > max_meals or user_input < min_meals:
            print("Are you sure of that ?")
        else:
            print(f"You chosed {user_input} meals")
            is_ok = False
    return user_input


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
        return int(round(counted, 2))

    def return_name(self, prod_input):
        for _ in range(0, self.len_of_names):
            if self.data["arkusz1"][_]["testName"] == prod_input:
                name = prod_input
        return name

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


    def bmi_calc(self, height, weight):
        bmi = weight/((height/100)*(height/100))
        result = round(bmi, 2)
        if result >= 40:
            bmi_result = "its 3rd degree obesity"
        elif (result >= 35) and (result <= 39.9):
            bmi_result = "its 2rd degree obesity"
        elif (result >= 30) and (result <= 34.9):
            bmi_result = "ts 1rd degree obesity"
        elif (result >= 25) and (result <= 29.9):
            bmi_result = " its overweight"
        elif (result >= 18.5) and (result <= 24.9):
            bmi_result = " its correct weight"
        elif (result >= 17) and (result <= 18.5):
            bmi_result = " its underweight"
        elif (result >= 16) and (result <= 16.9):
            bmi_result = " its emaciation"
        else :
            bmi_result = " its starvation"

        return f" Your BMI is : {result}, {bmi_result}"

    def calories_calc(self, gender, work, weight, height, age):
        if gender == "male" :
            BMR = (9.99*weight)+(6.25*height)-(5*age)+5 + 300
        else:
            BMR = (9.99 * weight) + (6.25 * height) - (5 * age) - 161 + 300

        if work == "Sitting job":
            CPM = BMR * 1.2
        elif work == "Middle intensity":
            CPM = BMR * 1.5
        else:
            CPM = BMR * 1.8

        return f"Your total metabolism is :  {CPM} kcal"