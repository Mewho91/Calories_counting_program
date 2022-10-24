
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
    product_input = input("Please add a product?\n").lower()
    gramature_input = int(input("how much grams?\n").lower())
    finished = str(input("Have you finished on this meal? 'y' for yes or 'n' for no \n")).lower()
    if finished == "y":
      end = False
    else :
      end = True