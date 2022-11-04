import functions
import gui


fc = functions.Functions()
g = gui.Gui()
# START
print("Welcome to calories counting program!")
MAX_MEALS = 8
MIN_MEALS = 1


g.open_popup()
number_of_meals = g.meal_count

d = {}

for meals in range(0, number_of_meals):

    calories = 0
    proteins = 0
    carbo = 0
    fat = 0

    end = True
    while end:
        g.run_gui()
        print(f"your {meals + 1} meal")
        # _________________________________product input musisz dokladnie wpisywac to co jest na liscie.
        product_input = g.product
        # product_input = input(f"Please chose a product to add {fc.name_chose()}\n")
        grams_input = g.gram
        # grams_input = int(input("how much grams of this product ?\n"))
        finished = str(input("Have you finished on this meal? 'y' for yes or 'n' for no \n")).lower()
        calories += fc.count(product_input, grams_input, functions.Data.CALORIES.value)
        proteins += fc.count(product_input, grams_input, functions.Data.PROT.value)
        carbo += fc.count(product_input, grams_input, functions.Data.CARBS.value)
        fat += fc.count(product_input, grams_input, functions.Data.FAT.value)
        if finished == "y":
            print(f"Your {meals + 1} Meal is  calories:  {calories}, proteins: {proteins},carbohydrates: {carbo},"
                  f" fat: {fat}")

            end = False
    d["Meal {0}".format(meals + 1)] = {"Cal": calories, "prot": proteins, "carb": carbo, "fat": fat}

print(f"{d} From {number_of_meals} Meals \n {(fc.sum_of_all_meals(d))}")
