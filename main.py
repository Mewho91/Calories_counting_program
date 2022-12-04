import functions
import gui


while True:
    fc = functions.Functions()
    g = gui.Gui()
    g.opening_window()
    g.first_window()
    g.all_counting()

    sums = g.sum_of_all(g.list_cals, g.list_prots, g.list_carbs, g.list_fat)
    g.what_u_added_to_meal(g.meals_name_and_gramature)
    g.last_window(g.result_list, sums)

    reset = g.y
    if reset == 0:
        pass
    else:
        break
