import functions

fc = functions.Functions()
# START
print("Welcome to calories counting program!")
MAX_MEALS = 8
MIN_MEALS = 1
is_ok = True

while is_ok:

    user_input = int(input("Select how many meals do you want to count? \n"))
    if user_input > MAX_MEALS or user_input < MIN_MEALS:
        print("Are you sure of that ?")
    else:
        print(f"You chosed {user_input} meals")
        is_ok = False
d ={}
for meals in range(0, user_input):
    calories = 0
    proteins = 0
    carbo = 0
    fat = 0

    end = True
    while end:
        print(f"your {meals + 1} meal")
        # _____________________________product input musisz dokladnie wpisywac to co jest na liscie.
        product_input = input(f"Please chose a product to add {fc.name_chose()}\n")
        gramature_input = int(input("how much grams of this product ?\n"))
        finished = str(input("Have you finished on this meal? 'y' for yes or 'n' for no \n")).lower()
        calories += fc.count_calories(product_input, gramature_input)
        proteins += fc.count_protein(product_input, gramature_input)
        carbo += fc.count_carb(product_input, gramature_input)
        fat += fc.count_fat(product_input, gramature_input)
        if finished == "y":
            print(f"Your {meals + 1} Meal is  calories:  {calories}, proteins: {proteins},carbohydrates: {carbo}, fat: {fat}")
            end = False
    d["Meal {0}".format(meals+1)] = {"Cal" : calories, "prot": proteins, "carb" : carbo, "fat" : fat}

print(fc.sum_of_all_meals(d))