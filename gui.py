import os.path
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import functions
import json


class Gui:
    def __init__(self):

        self.y = None
        self.meal_count = 0
        self.product = None
        self.gram = 0
        self.box_value = None
        self.product_value = None
        self.entry_value = None
        self.finished = False
        self.m_f = ""
        self.weight = 0
        self.height = 0
        self.age = 0
        self.work = ""
        self.list_to_be_loaded = ""

    def opening_window(self):
        fc = functions.Functions()
        root = Tk()
        root.title("Hello")
        canvas = Canvas(root, width=650, height=450)
        canvas.pack()
        opening_img = PhotoImage(file="dnavege.png")
        canvas.create_image(0, 0, image=opening_img, anchor="nw")
        canvas.create_text(200, 20, text="Hello welcome to the program", font=("Times", "20", "bold"))

        self.male_female = StringVar()
        male_or_female_box = Combobox(root, width=10, font=("Times", "15"), state='readonly',
                                     textvariable=self.male_female)
        male_or_female_box.pack()
        male_or_female_box['values'] = ("Male", "Female")
        canvas.create_window(100, 110,height=20, anchor="nw", window=male_or_female_box)
        canvas.create_text(390, 120, text="Please select a gender", font=("Times", "20", "bold"), fill="blue")

        self.entry_body_weight = IntVar()
        weight_entry = Entry(width=12, font=("Times", "15", "bold"), background="black",
                             textvariable=self.entry_body_weight)
        canvas.create_window(100, 150, height=20, anchor="nw", window=weight_entry)
        canvas.create_text(450, 160, text="Enter your weight in kilograms", font=("Times", "20", "bold"), fill="blue")

        self.entry_body_height = IntVar()
        body_height = Entry(width=12, font=("Times", "15", "bold"), background="black",
                             textvariable=self.entry_body_height)
        canvas.create_window(100, 190, height=20, anchor="nw", window=body_height)
        canvas.create_text(370, 200, text="Enter your height", font=("Times", "20", "bold"), fill="blue")

        self.age_int = IntVar()
        age = Entry(width=12, font=("Times", "15", "bold"), background="black",
                             textvariable=self.age_int)
        canvas.create_window(100, 230, height=20, anchor="nw", window=age)
        canvas.create_text(350, 240, text="Enter your age", font=("Times", "20", "bold"), fill="blue")

        self.work_entry = StringVar()
        work_entry = Combobox(root, width=10, font=("Times", "15"), state='readonly',
                                     textvariable=self.work_entry)
        work_entry['values'] = ("Sitting job", "Middle intensity", "High intensity")
        canvas.create_window(100, 280, height=20, anchor="nw", window=work_entry)
        canvas.create_text(385, 290, fill="blue", font=("Times", "20", "bold"), text="Enter work intensity")

        process_button = Button(root, width=30, text="Count BMI and caloric needs",
                                command=lambda: [self.body_weight(),self.mf_func(),  self.body_weight(),
                                                 self.body_height(),
                                                 self.user_age(), self.work_intensity(), fc.bmi_calc(self.height, self.weight),
                                                 fc.calories_calc(self.m_f, self.work, self.weight, self.height, self.age),
                                                 self.is_process_button_pressed()])
        canvas.create_window(420, 400, height=30, anchor="nw", window=process_button)

        load_diet_button = Button(root, width=30, text="Load diet")
        canvas.create_window(220, 400, height=30, anchor="nw", window=load_diet_button)

        pass_bmi_count = Button(root, width=30, text="Skip calculator", command=root.destroy)
        canvas.create_window(20, 400, height=30, anchor="nw", window=pass_bmi_count)

        root.mainloop()

    def is_process_button_pressed(self):
        fc = functions.Functions()
        tkinter.messagebox.showinfo(title="Results",
                                    message=f"{fc.bmi_calc(self.height, self.weight)},"
                                            f"\n{fc.calories_calc(self.m_f, self.work, self.weight, self.height, self.age)}")

    def mf_func(self):
        self.m_f = self.male_female.get()

    def body_weight(self):
        self.weight = int(self.entry_body_weight.get())

    def body_height(self):
        self.height = int(self.entry_body_height.get())

    def user_age(self):
        self.age = int(self.age_int.get())

    def work_intensity(self):
        self.work = self.work_entry.get()

    def first_window(self):
        root = Tk()
        root.title("Number of meals")

        my_img = PhotoImage(file="vegetables.png")

        canvas = Canvas(root, width=600, height=380)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(10, 0, image=my_img, anchor="nw")
        canvas.create_text(280, 100, text="Welcome to calories counting program",fill="white",
                           font=("Times", "23", "bold"))
        canvas.create_text(280, 220, text="Chose number of meals and press confirm",fill="white",
                           font=("Times", "20", "bold"))
        self.box_value = StringVar()
        meal_chose_scroll = Combobox(root, width=20, font=("Times", "15"), state='readonly',
                                     textvariable=self.box_value)
        meal_chose_scroll['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
        meal_chose_scroll.current(0)
        meal_chose_scroll.pack()
        button1 = Button(root, width=30,  text="Confirm", command=lambda: [self.meal_number_get(), root.destroy()])
        canvas.create_window(350, 300, height=50, anchor="nw", window=button1)
        canvas.create_window(50, 300,height=50, anchor="nw", window=meal_chose_scroll)

        root.mainloop()

    def meal_number_get(self):
        self.meal_count = int(self.box_value.get())

    def secound_window(self):
        fc = functions.Functions()
        root = Tk()
        root.title("Calories count program")

        my_img = PhotoImage(file="second window.png")
        canvas = Canvas(root, width=470, height=650)
        canvas.pack()
        canvas.create_image(10, 0, image=my_img, anchor="nw")
        canvas.create_text(200, 40, text="Chose a product name", fill="white",
                           font=("Times", "23", "bold"))

        self.product_value = StringVar()
        scroll = Combobox(root, font=("Times", "15", "bold"), state='readonly', textvariable=self.product_value)
        scroll['values'] = (fc.name_chose())
        scroll.current(0)
        canvas.create_window(40, 100, height=50, width=250, anchor="nw", window=scroll)

        self.entry_value = IntVar()
        entry = Entry(width=25, font=("Times", "25", "bold"), background="red", textvariable=self.entry_value)
        canvas.create_window(40, 300, height=50, width=250, anchor="nw", window=entry)
        canvas.create_text(240, 240, fill="white", font=("Times", "23", "bold"), text="Enter a gramature of product")

        button1 = Button(text="Confirm", width=50, command=lambda: [self.product_get(), self.product_gram(),
                                                                    root.destroy()])
        canvas.create_window(40, 400, height=50, anchor="nw", window=button1)

        root.mainloop()

    def product_get(self):
        self.product = self.product_value.get()

    def product_gram(self):
        self.gram = int(self.entry_value.get())

    def third_window(self, x):
        root = Tk()
        root.title("Next meal ?")

        my_img = PhotoImage(file="third window.png")
        canvas = Canvas(root, width=520, height=350)
        canvas.pack()
        canvas.create_image(0, 0, image=my_img, anchor="nw")

        canvas.create_text(250, 30, text=f"You added {self.product} : {self.gram} grams", font=("Times", "20", "bold"))
        canvas.create_text(250, 200, text=x, font=("Times", "15", "bold"))

        button_next_meal = Button(root, text="Go to next meal", command=lambda: [self.next(), root.destroy()])
        canvas.create_window(100, 300, height=50, anchor="nw", window=button_next_meal)

        button_this_meal = Button(root, text="Add product to this meal", command=lambda: [self.this(), root.destroy()])
        canvas.create_window(300, 300, height=50, anchor="nw", window=button_this_meal)

        root.mainloop()

    def next(self):
        self.finished = True

    def this(self):
        self.finished = False

    def last_window(self, r, sums):
        result_window = Tk()
        result_window.title("Results")

        my_img = PhotoImage(file="notebook.png")
        canvas = Canvas(result_window, width=660, height=860)
        canvas.pack()
        canvas.create_image(0, 0, image=my_img, anchor="nw")

        for item in r:
            canvas.create_text(310, 120 + r.index(item) * 80,
                               text=item.replace("'", " ").replace("]", " ").replace("[", " "),
                               font=("Times", "14"))
        canvas.create_text(320, 680, text=sums, font=("Times", "15", "bold"))
        restart_button = Button(text="Restart program", command=lambda: [self.restart_program(),
                                                                         result_window.destroy()])
        canvas.create_window(100, 750, width=100, height=80, window=restart_button)
        result_button = Button(text="Close program", command=lambda: [self.close_program(), result_window.destroy()])
        canvas.create_window(550, 750, width=100, height=80, window=result_button)
        save_button = Button(text="Save diet", command=lambda: [result_window.destroy(), self.save_diet()])
        canvas.create_window(300, 750, width=100, height=80, window=save_button)

        result_window.mainloop()

    def sum_of_all(self, cal, prot, carb, fat):
        self.sum_cal = sum(cal)
        self.sum_prot = sum(prot)
        self.sum_carb = sum(carb)
        self.sum_fat = sum(fat)
        self.summary = f"Summary calories : {self.sum_cal}, proteins :  {self.sum_prot}, carbs : {self.sum_carb}, " \
                       f"fat: {self.sum_fat}"
        return self.summary

    def prods(self, prod_input, gram_input, meal):
        return f"Meal {meal + 1} - Product : {prod_input}, grams : {gram_input}"

    def dict_prods(self, prod_input, gram_input):
        dictio = f"({prod_input, gram_input}"
        return dictio

    def what_u_added_to_meal(self, d):
        values = []
        for a in d:
            values.append(f"In {a} you added ")
            for b in d[a]:
                values.append(f"{b[0]} {b[1]} grams")
        return values

    def return_list_added(self, l):
        val = []
        for i in l:
            val.append(i)
        new_val = ("".join(val).replace(",", "\n"))
        if len(new_val) > 1:
            return f"Your meal contains:\n {new_val}"

    def restart_program(self):
        self.y = 0
        return self.y

    def close_program(self):
        self.y = 1
        return self.y

    def save_diet(self):
        save_window = Tk()
        save_window.title("Save window")

        image = PhotoImage(file="save load window.png")
        canvas = Canvas(save_window, width=800, height=350)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor="nw")

        self.user_input = StringVar()
        self.user_name_input = Entry(width=33, textvariable=self.user_input)
        user_name_label = Label(text="Insert name of diet", font=("Times", 20))
        canvas.create_window(500,100, window=self.user_name_input)
        canvas.create_window(200,100, window=user_name_label)

        save_button = Button(text="Save", command=self.save)
        canvas.create_window(300,200, window=save_button)
        exit = Button(text="Exit", command=save_window.destroy)
        canvas.create_window(500,200, window=exit)

        save_window.mainloop()

    def save(self):
        self.save_name = self.user_input.get()
        new_data = {self.save_name: {
                "contents": self.result_list,
                "macronutrients": self.summary
                }
        }
        try:
            with open("dietdata.json", "r") as dt:
                dtjson = json.load(dt)
        except FileNotFoundError:

            with open("dietdata.json", "w") as dt:
                json.dump(new_data, dt, indent=2)
        else:
            dtjson.update(new_data)
            with open("dietdata.json", "w") as dt:
                json.dump(dtjson, dt, indent=2)

    def load_diet(self):
        load = Tk()
        load.title("Load window")

        image = PhotoImage(file="load_diet.png")
        canvas = Canvas(load, width=700, height=500)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor="nw")

        self.load_lists = StringVar()
        scroll = Combobox(load, font=("Times", "15", "bold"), state='readonly', textvariable=self.load_lists)
        scroll['values'] = self.load_diet_lists_by_names()
        canvas.create_window(40, 100, height=50, width=250, anchor="nw", window=scroll)

        load_button = Button(text="Load", command=lambda:[self.load_get(), self.search_for_loaded_list()])
        canvas.create_window(300, 200, window=load_button)

        load.mainloop()

    def load_get(self):
        self.list_to_be_loaded = str(self.load_lists.get())

    def load_diet_lists_by_names(self):
        f = open('dietdata.json')
        data = json.load(f)

        self.list_of_diets = []
        for d in data:
            self.list_of_diets.append(d)

        return self.list_of_diets

    def search_for_loaded_list(self):
        f = open('dietdata.json')
        data = json.load(f)

        return print(data[self.list_to_be_loaded])

    def all_counting(self):
        fc = functions.Functions()
        d = {}
        self.list_cals = []
        self.list_prots = []
        self.list_carbs = []
        self.list_fat = []
        self.meals_name_and_gramature = {}

        for meals in range(0, self.meal_count):

            calories = 0
            proteins = 0
            carbo = 0
            fat = 0
            list_of_prod = []

            end = True
            while end:

                self.secound_window()
                product_input = self.product
                grams_input = self.gram
                finished = self.third_window(self.return_list_added(list_of_prod))
                calories += fc.count(product_input, grams_input, functions.Data.CALORIES.value)
                proteins += fc.count(product_input, grams_input, functions.Data.PROT.value)
                carbo += fc.count(product_input, grams_input, functions.Data.CARBS.value)
                fat += fc.count(product_input, grams_input, functions.Data.FAT.value)
                list_of_prod.append(f"{product_input} {grams_input}g")
                if self.finished:
                    self.meals_name_and_gramature[f"Meal {meals + 1}"] = list_of_prod
                    end = False

            d["Meal {0}".format(meals + 1)] = {"Cal": calories, "prot": proteins, "carb": carbo, "fat": fat}
            self.list_cals.append(d[f'Meal {meals + 1}']['Cal'])
            self.list_prots.append(d[f'Meal {meals + 1}']['prot'])
            self.list_carbs.append(d[f'Meal {meals + 1}']['carb'])
            self.list_fat.append(d[f'Meal {meals + 1}']['fat'])

        self.result_list = []

        for m in range(0, self.meal_count):
            self.result_list.append(f"Meal {m + 1}: \n "
                               f"{self.meals_name_and_gramature[f'Meal {m + 1}']}\n "
                               f"Calories : {self.list_cals[m]}, "
                               f"Proteins :{self.list_prots[m]}, "
                               f"Carbohydrates : {self.list_carbs[m]},"
                               f"Fat :{self.list_fat[m]}\n")
