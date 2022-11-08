import functions
import gui


fc = functions.Functions()
g = gui.Gui()

g.open_popup()
number_of_meals = g.meal_count

d = {}
list_cals = []
list_prots = []
list_carbs = []
list_fat = []
list_m =[]
list_names =[]


for meals in range(0, number_of_meals):

    calories = 0
    proteins = 0
    carbo = 0
    fat = 0
    # ----------------------------------- udalo sie zrobic listę nazw na koncu wyprintowana
    end = True
    while end:
        g.run_gui()
        print(f"your {meals + 1} meal")
        product_input = g.product
        grams_input = g.gram
        finished = g.next_meal()
        list_names.append(fc.return_name(product_input))
        calories += fc.count(product_input, grams_input, functions.Data.CALORIES.value)
        proteins += fc.count(product_input, grams_input, functions.Data.PROT.value)
        carbo += fc.count(product_input, grams_input, functions.Data.CARBS.value)
        fat += fc.count(product_input, grams_input, functions.Data.FAT.value)
        if g.finished:
            print(f"Your {meals + 1} Meal is  calories:  {calories}, proteins: {proteins},carbohydrates: {carbo},"
                  f" fat: {fat}")
            # g.add_label()

            end = False
    d["Meal {0}".format(meals + 1)] = {"Cal": calories, "prot": proteins, "carb": carbo, "fat": fat}
    list_cals.append(d[f'Meal {meals + 1}']['Cal'])
    list_prots.append(d[f'Meal {meals + 1}']['prot'])
    list_carbs.append(d[f'Meal {meals + 1}']['carb'])
    list_fat.append(d[f'Meal {meals + 1}']['fat'])
    # list_names.append(d[f'Meal {meals + 1}']['testName'])
    # name = d[f'Meal {meals + 1}']['testName']
    # g.add_label(name)
    list_m.append(meals)

result_list = []
for m in range (0, number_of_meals):
    print(m)
    result_list.append(f" Meal {m+1} has Calories : {list_cals[m]}, Proteins :{list_prots[m]}, Carbohydrates : {list_carbs[m]},"
          f" Fat :{list_fat[m]}\n")
sums = g.sum_of_all(list_cals, list_prots, list_carbs, list_fat)
g.results(result_list, sums)

print(list_names)
