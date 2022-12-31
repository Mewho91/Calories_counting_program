import functions
import gui
import json

dict = {'contents': ["Meal 1: \n ['Banan 111g', 'Banan 200g']\n Calories : 273, Proteins :3, Carbohydrates : 71,Fat :0\n", "Meal 2: \n ['Banan 200g', 'Banan 500g']\n Calories : 616, Proteins :7, Carbohydrates : 161,Fat :1\n", "Meal 3: \n ['Banan 23535g']\n Calories : 20710, Proteins :258, Carbohydrates : 5413,Fat :70\n"], 'macronutrients': 'Summary calories : 21599, proteins :  268, carbs : 5645, fat: 71'}

result = dict['contents']
sumary = dict['macronutrients']

print(result)
print(sumary)

for i in result:
    print(i)