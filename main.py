import functions
import gui


while True:
    fc = functions.Functions()
    g = gui.Gui()
    g.first_window()
    number_of_meals = g.meal_count

    d = {}
    list_cals = []
    list_prots = []
    list_carbs = []
    list_fat = []
    meals_name_and_gramature = {}

    for meals in range(0, number_of_meals):

        calories = 0
        proteins = 0
        carbo = 0
        fat = 0
        list_of_prod = []

        end = True
        while end:

            g.secound_window()
            product_input = g.product
            grams_input = g.gram
            finished = g.third_window(g.return_list_added(list_of_prod))
            calories += fc.count(product_input, grams_input, functions.Data.CALORIES.value)
            proteins += fc.count(product_input, grams_input, functions.Data.PROT.value)
            carbo += fc.count(product_input, grams_input, functions.Data.CARBS.value)
            fat += fc.count(product_input, grams_input, functions.Data.FAT.value)
            list_of_prod.append(f"{product_input} {grams_input}g")

            if g.finished:
                meals_name_and_gramature[f"Meal {meals + 1}"] = list_of_prod
                end = False

        d["Meal {0}".format(meals + 1)] = {"Cal": calories, "prot": proteins, "carb": carbo, "fat": fat}
        list_cals.append(d[f'Meal {meals + 1}']['Cal'])
        list_prots.append(d[f'Meal {meals + 1}']['prot'])
        list_carbs.append(d[f'Meal {meals + 1}']['carb'])
        list_fat.append(d[f'Meal {meals + 1}']['fat'])

    result_list = []

    for m in range (0, number_of_meals):

        result_list.append(f"Meal {m+1}: \n "
                           f"{meals_name_and_gramature[f'Meal {m+1}']}\n "
                           f"Calories : {list_cals[m]}, "
                           f"Proteins :{list_prots[m]}, "
                           f"Carbohydrates : {list_carbs[m]},"
                           f"Fat :{list_fat[m]}\n")

    sums = g.sum_of_all(list_cals, list_prots, list_carbs, list_fat)
    g.what_u_added_to_meal(meals_name_and_gramature)
    g.last_window(result_list, sums)
    print(result_list)

    reset = g.y
    if reset == 0:
        pass
    else:
        break
