import playground

import_class = playground.Playground()
print("Welcome to calories counting program!")
MAX_MEALS = 8
MIN_MEALS = 1
is_ok = True
while is_ok :
  user_input = int(input("Select how many meals do you want to count? \n"))
  if user_input > MAX_MEALS or user_input < MIN_MEALS:
    print("Are you sure of that ?")
  else :
    print(f"You chosed {user_input} meals")
    is_ok = False
for _ in range(0, user_input):
  end = True
  while end:
    print(f"your {_+1} meal")
    # _____________________________product input musisz dokladnie wpisywac to co jest na liscie.
    product_input = input(f"Please chose a product to add {import_class.name_chose()}\n")
    gramature_input = int(input("how much grams of this product ?\n"))
    print(import_class.data_by_name(product_input, gramature_input))
    finished = str(input("Have you finished on this meal? 'y' for yes or 'n' for no \n")).lower()
    if finished == "y":
      end = False
    else :
      end = True