import gui

g = gui.Gui()
end = True
g.open_popup()
print(g.meal_number_get())

while end:
    g.run_gui()
    print(g.product_gram())
    print(g.product_get())
