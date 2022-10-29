dict = {
    'Meal 1': {'Cal': 164.0, 'prot': 31.0, 'carb': 0.0, 'fat': 3.6},
    'Meal 2': {'Cal': 250.0, 'prot': 26.0, 'carb': 0.0, 'fat': 15.0}
        }


# print(dict['Meal 1']['Cal'])
sum_cal = []
sum_prot =[]
sum_carb = []
sum_fat = []
for key in dict:
    sum_cal.append(dict[key]['Cal'])
    sum_prot.append(dict[key]['prot'])
    sum_carb.append(dict[key]['carb'])
    sum_fat.append(dict[key]['fat'])

print(sum(sum_cal))
print(sum(sum_prot))
print(sum(sum_carb))
print(sum(sum_fat))

