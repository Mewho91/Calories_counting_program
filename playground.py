import functions
import gui
import json

g = gui.Gui()
f = functions.Functions()

# f = open('dietdata.json')
# data = json.load(f)
# a = "aaa"
# print(data[a])
g.load_diet()

